# Web Scraper de Livros com Scrapy

Projeto de automacao em Python utilizando o framework Scrapy para extracao, filtragem e exportacao de dados do site [Books to Scrape](http://books.toscrape.com/).

---

## Funcionalidades

- Crawl com paginacao automatica: navega por todas as paginas do catalogo recursivamente
- Filtro de qualidade: extrai apenas livros com avaliacao de 4 ou 5 estrelas
- Dados estruturados: titulo, preco (normalizado como float), avaliacao e disponibilidade
- Exportacao em JSON via Feed Export do Scrapy
- Pipeline de limpeza: trata campos nulos e normaliza o preco
- Tratamento de erros e logging integrados

---

## Estrutura do projeto

```
web-scraper-scrapy/
├── scrapy.cfg                      # Configuracao do projeto Scrapy
├── requirements.txt                # Dependencias (scrapy)
├── books.json                      # Output gerado pelo crawler
│
├── booksscraper/                   # Pacote principal
│   ├── __init__.py
│   ├── items.py                    # BookItem: definicao dos campos extraidos
│   ├── pipelines.py                # PriceNormalizationPipeline: limpeza dos dados
│   ├── settings.py                 # Configuracoes do crawler (delay, user-agent, etc.)
│   │
│   └── spiders/                    # Spiders do projeto
│       ├── __init__.py
│       └── books_spider.py         # Spider principal: parse, paginacao, errback
│
└── tests/                          # Testes automatizados
    ├── __init__.py
    └── test_pipeline.py            # Testes do pipeline e do filtro de estrelas
```

### Descricao dos arquivos principais

| Arquivo | Responsabilidade |
|---|---|
| `booksscraper/items.py` | Define `BookItem` com os campos `title`, `price`, `rating`, `availability` |
| `booksscraper/pipelines.py` | `PriceNormalizationPipeline`: converte preco para float, trata `None` com valores padrao |
| `booksscraper/settings.py` | Configuracoes do Scrapy: `DOWNLOAD_DELAY`, `CONCURRENT_REQUESTS`, `ROBOTSTXT_OBEY`, `FEEDS`, pipeline ativo |
| `booksscraper/spiders/books_spider.py` | Spider `books`: navega todas as paginas, filtra 4-5 estrelas, loga erros |
| `tests/test_pipeline.py` | 11 testes unitarios para pipeline e filtro de estrelas |

---

## Tecnologias

- **Python 3.x**
- **Scrapy 2.16** — Framework de Web Crawling
- **pytest** — Testes unitarios

---

## Como executar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Executar o crawler

```bash
scrapy crawl books
```

Para limitar a paginas de teste:

```bash
scrapy crawl books -s CLOSESPIDER_PAGECOUNT=2
```

### 3. Rodar os testes

```bash
python -m pytest tests/ -v
```

### 4. Resultado

O arquivo `books.json` sera gerado automaticamente na raiz do projeto.

---

## Exemplo de output

```json
[
    {
        "title": "Sharp Objects",
        "price": 47.82,
        "rating": "Four",
        "availability": "In stock"
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "price": 54.23,
        "rating": "Five",
        "availability": "In stock"
    }
]
```

---

## Autor

**Christiano Goncalves Araujo**
Engenharia de Software - PUC Minas
[LinkedIn](https://www.linkedin.com/in/christiano-gonara) | [GitHub](https://github.com/christiano-gonara)