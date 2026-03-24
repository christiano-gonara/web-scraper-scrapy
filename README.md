# 🕷️ Book Scraper com Scrapy

Projeto de automação desenvolvido em **Python** utilizando o framework **Scrapy** para extração de dados do site *Books to Scrape*.

## 🚀 Funcionalidades
- Realiza o crawling completo de múltiplas páginas de livros.
- **Filtro de Qualidade:** O script filtra automaticamente apenas livros com avaliação de **4 ou 5 estrelas**.
- Extrai título, preço, avaliação e disponibilidade em estoque.
- Exporta os resultados finais em um arquivo estruturado `books.json`.

## 🛠️ Tecnologias
- **Python 3.x**
- **Scrapy** (Framework de Web Crawling)
- **JSON** (Formato de saída)

## 📋 Como executar
1. Certifique-se de ter o Scrapy instalado: `pip install scrapy`
2. Execute o script: `python nome_do_seu_arquivo.py`
3. O arquivo `books.json` será gerado automaticamente com os dados filtrados.
