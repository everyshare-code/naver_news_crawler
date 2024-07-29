DEFAULT_CONFIG = {
    "urls": {
        "base": "https://news.naver.com",
        "categories": {
            "flash": {
                "url": "/main/list.naver",
                "params": {
                    "mode": "LSD",
                    "mid": "sec",
                    "sid1": "001"
                }
            },
            "politics": {
                "url": "/section/100"
            },
            "economy": {
                "url": "/section/101"
            },
            "social": {
                "url": "/section/102"
            },
            "life": {
                "url": "/section/103"
            },
            "it": {
                "url": "/section/105"
            },
            "world": {
                "url": "/section/104"
            }
        }
    }
}
