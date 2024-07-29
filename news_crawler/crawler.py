import ray
from news_crawler.url_constructor import construct_url
from news_crawler.fetch_details import fetch_article_details
from news_crawler.config import DEFAULT_CONFIG
from playwright.sync_api import sync_playwright

@ray.remote
def fetch_article_links(base_url: str, category_info: dict, category: str):
    url = construct_url(base_url, category_info)
    article_links = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Navigating to URL: {url}")
        page.goto(url)
        page.wait_for_load_state('networkidle')
        print("Page loaded and network is idle")

        try:
            if category == 'flash':
                locator = page.locator("xpath=//*[@id='main_content']/div[2]/ul[1]/li")
            else:
                locator = page.locator("xpath=//*[contains(@id, 'SECTION_HEADLINE_LIST')]/li")

            elements = locator.all()
            print(f"Number of elements found: {len(elements)}")

            for element in elements[:5]:
                link_element = element.locator("a").first
                link = link_element.get_attribute("href")
                article_links.append(link)
        except Exception as e:
            print(f"An error occurred: {e}")

        browser.close()

    return article_links

def crawl_naver_news(category: str, base_url=None, categories=None):
    config = DEFAULT_CONFIG
    if base_url:
        config['urls']['base'] = base_url
    if categories:
        config['urls']['categories'].update(categories)

    ray.init(num_cpus=10)

    category_info = config['urls']['categories'][category]
    future_links = fetch_article_links.remote(config['urls']['base'], category_info, category)
    article_links = ray.get(future_links)

    futures_details = [fetch_article_details.remote(link) for link in article_links]
    article_details = ray.get(futures_details)

    return article_details

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Crawl Naver News")
    parser.add_argument('category', type=str, help='News category to crawl')

    args = parser.parse_args()
    news_data = crawl_naver_news(args.category)
    print(news_data)

