import psycopg2
from itemadapter import ItemAdapter


class PriceNormalizationPipeline:
    # Normaliza e limpa os campos de cada item antes da exportacao
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Converte preco de string com simbolo (£) para float
        price = adapter.get('price')
        if price:
            try:
                adapter['price'] = float(price.replace('\u00a3', '').replace('£', '').strip())
            except (ValueError, AttributeError):
                spider.logger.warning(f"Could not parse price: {price}")
                adapter['price'] = 0.0
        else:
            adapter['price'] = 0.0

        # Define valores padrao para campos nulos
        adapter['title'] = adapter.get('title') or 'Unknown Title'
        adapter['rating'] = adapter.get('rating') or 'Unknown'
        adapter['availability'] = adapter.get('availability') or 'Unknown'

        return item


class PostgreSQLPipeline:
    # Conecta ao banco e cria a tabela ao iniciar o crawler
    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            host=spider.settings.get('DB_HOST', 'localhost'),
            port=spider.settings.get('DB_PORT', '5432'),
            dbname=spider.settings.get('DB_NAME', 'books'),
            user=spider.settings.get('DB_USER', 'postgres'),
            password=spider.settings.get('DB_PASSWORD', ''),
        )
        self.conn.autocommit = True
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    price NUMERIC(10,2) NOT NULL,
                    rating TEXT NOT NULL,
                    availability TEXT NOT NULL
                )
            """)
        spider.logger.info("PostgreSQL pipeline ready.")

    # Insere cada item extraido no banco de dados
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO books (title, price, rating, availability) VALUES (%s, %s, %s, %s)",
                (adapter['title'], adapter['price'], adapter['rating'], adapter['availability']),
            )
        spider.logger.debug(f"Inserted: {adapter['title']}")
        return item

    # Fecha a conexao ao finalizar o crawler
    def close_spider(self, spider):
        self.conn.close()
        spider.logger.info("PostgreSQL connection closed.")