from itemadapter import ItemAdapter


class PriceNormalizationPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        price = adapter.get('price')
        if price:
            try:
                adapter['price'] = float(price.replace('\u00a3', '').replace('£', '').strip())
            except (ValueError, AttributeError):
                spider.logger.warning(f"Could not parse price: {price}")
                adapter['price'] = 0.0
        else:
            adapter['price'] = 0.0

        adapter['title'] = adapter.get('title') or 'Unknown Title'
        adapter['rating'] = adapter.get('rating') or 'Unknown'
        adapter['availability'] = adapter.get('availability') or 'Unknown'

        return item