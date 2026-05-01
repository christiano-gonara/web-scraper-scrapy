# 🕷️ Web Scraper de Livros | Scrapy + Python
 
Projeto de automação desenvolvido em Python utilizando o framework **Scrapy** para extração, filtragem e análise de dados do site [Books to Scrape](http://books.toscrape.com/).
 
---
 
## 🚀 Funcionalidades
 
- **Crawling com Paginação Automática:** Navega por todas as páginas do catálogo recursivamente via `response.follow`.
- **Filtro de Qualidade:** Extrai apenas livros com avaliação de **4 ou 5 estrelas**, ignorando os demais.
- **Extração Estruturada:** Coleta título, preço, avaliação e disponibilidade em estoque de cada livro.
- **Exportação em JSON:** Salva os resultados em `books.json` apenas ao final do crawling completo, evitando escritas parciais.
---
 
## 🛠️ Tecnologias
 
- **Python 3.x**
- **Scrapy** — Framework de Web Crawling
- **JSON** — Formato de saída estruturada
---
 
## 📊 Exemplo de Output
 
```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "rating": "Three",
    "availability": "In stock"
  }
]
```
 
---
 
## ⚙️ Como executar
 
**1. Instalar dependências**
 
```bash
pip install scrapy
```
 
**2. Executar o crawler**
 
```bash
python books.py
```
 
**3. Resultado**
 
O arquivo `books.json` será gerado automaticamente com os livros filtrados.
 
---
 
## 👤 Autor
 
**Christiano Gonçalves Araujo**  
Engenharia de Software - PUC Minas  
[LinkedIn](https://www.linkedin.com/in/christiano-gonara) | [GitHub](https://github.com/christiano-gonara)
