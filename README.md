
# 📰 Naver News Crawler

네이버 뉴스에서 원하는 카테고리의 헤드라인 뉴스를 가져오는 Python 모듈입니다.

## 카테고리
- `it`: IT/과학
- `politics`: 정치
- `economy`: 경제
- `social`: 사회
- `life`: 생활/문화
- `world`: 세계
- `flash`: 속보

## 📦 설치

GitHub에서 직접 모듈을 설치할 수 있습니다. 다음 명령어를 사용하여 설치하십시오:

```bash
pip install git+https://github.com/yourusername/naver_news_crawler.git
```

설치가 완료되면 `playwright` 브라우저를 설치해야 합니다:

```bash
playwright install
```

## 🛠️ 사용 방법

### 프로그래밍 방식 사용 방법

Python 코드 내에서 직접 모듈을 사용할 수 있습니다. 예시는 다음과 같습니다:

```python
from naver_news_crawler.crawler import crawl_naver_news

news_data = crawl_naver_news('it')
print(news_data)
```

### 예시

IT/과학 카테고리의 헤드라인 뉴스를 가져오는 예시입니다:

```python
from naver_news_crawler.crawler import crawl_naver_news

# IT/과학 카테고리 뉴스 가져오기
news_data = crawl_naver_news('it')
for article in news_data:
    print(f"Title: {article['title']}")
    print(f"Link: {article['article_link']}")
    print(f"Date: {article['date']}")
    print(f"Description: {article['description']}")
    print(f"Image: {article['image_link']}")
    print("-" * 80)
```

## 🤝 기여

기여를 환영합니다! 이슈를 등록하거나, 풀 리퀘스트를 보내주세요.

## 📧 문의

궁금한 사항이 있거나 문제가 발생한 경우, 아래 이메일로 연락주세요:

- Author: everyshare
- Email: park20542040@gmail.com
