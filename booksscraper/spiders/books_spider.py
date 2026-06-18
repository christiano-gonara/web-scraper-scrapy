import scrapy
from booksscraper.items import BookItem


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.books_list = []

    def parse(self, response):
        for book in response.css('article.product_pod'):
            estrelas = book.css('p.star-rating::attr(class)').get()

            if estrelas and ('Four' in estrelas or 'Five' in estrelas):
                item = BookItem(
                    title=book.css('h3 a::attr(title)').get(),
                    price=book.css('p.price_color::text').get(),
                    rating=estrelas.replace('star-rating ', ''),
                    availability=book.css('p.instock.availability::text').re_first(r'(\S+\s\S+)'),
                )
                self.books_list.append(item)
                yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse, errback=self.errback)
        else:
            self.logger.info(f"Crawling finished. {len(self.books_list)} books collected.")

    def errback(self, failure):
        self.logger.error(f"Request failed: {failure.request.url}")
        self.logger.error(repr(failure))