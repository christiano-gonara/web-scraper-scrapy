import scrapy
from scrapy.crawler import CrawlerProcess
import json

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']
    
    # Lista para acumular os dados
    books_list = []

    def parse(self, response):
        # Extrai os dados dos livros da página atual
        for book in response.css('article.product_pod'):
            estrelas = book.css('p.star-rating::attr(class)').get()
            
            # Filtro: Só pega se tiver 4 ou 5 estrelas
            if estrelas and ('Four' in estrelas or 'Five' in estrelas):
                book_data = {
                    'title': book.css('h3 a::attr(title)').get(),
                    'price': book.css('p.price_color::text').get(),
                    'rating': estrelas.replace('star-rating ', ''),
                    'availability': book.css('p.instock.availability::text').re_first(r'(\S+\s\S+)'),
                }
                self.books_list.append(book_data)

        # Caso haja próxima página
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            # Salva o JSON apenas no final
            with open('books.json', 'w', encoding='utf-8') as f:
                json.dump(self.books_list, f, ensure_ascii=False, indent=4)

# Execução do Crawler
process = CrawlerProcess()
process.crawl(BooksSpider)
process.start()