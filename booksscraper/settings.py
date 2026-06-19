import os

BOT_NAME = "booksscraper"

SPIDER_MODULES = ["booksscraper.spiders"]
NEWSPIDER_MODULE = "booksscraper.spiders"

# Respeita as regras do robots.txt do site alvo
ROBOTSTXT_OBEY = True

# Controles de taxa para nao sobrecarregar o servidor
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 4

# Identificacao do cliente HTTP
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Cadeia de pipelines executadas em ordem crescente de prioridade
ITEM_PIPELINES = {
    "booksscraper.pipelines.PriceNormalizationPipeline": 300,
    "booksscraper.pipelines.PostgreSQLPipeline": 400,
}

# Exportacao paralela para JSON via Feed Export do Scrapy
FEEDS = {
    "books.json": {
        "format": "json",
        "encoding": "utf-8",
        "indent": 4,
        "overwrite": True,
    },
}

# Configuracoes de conexao com PostgreSQL via variaveis de ambiente
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "books")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")