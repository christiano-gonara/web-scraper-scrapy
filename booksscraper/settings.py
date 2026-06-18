BOT_NAME = "booksscraper"

SPIDER_MODULES = ["booksscraper.spiders"]
NEWSPIDER_MODULE = "booksscraper.spiders"

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 4

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

ITEM_PIPELINES = {
    "booksscraper.pipelines.PriceNormalizationPipeline": 300,
}

FEEDS = {
    "books.json": {
        "format": "json",
        "encoding": "utf-8",
        "indent": 4,
        "overwrite": True,
    },
}