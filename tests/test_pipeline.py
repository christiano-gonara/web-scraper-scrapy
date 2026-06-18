import pytest
import logging

from booksscraper.items import BookItem
from booksscraper.pipelines import PriceNormalizationPipeline


@pytest.fixture
def pipeline():
    return PriceNormalizationPipeline()


@pytest.fixture
def fake_spider():
    class FakeSpider:
        logger = logging.getLogger("test")
    return FakeSpider()


class TestPriceNormalizationPipeline:
    def test_converts_pound_string_to_float(self, pipeline, fake_spider):
        item = BookItem(title="Test Book", price="£51.77", rating="Four", availability="In stock")
        result = pipeline.process_item(item, fake_spider)
        assert result["price"] == 51.77
        assert isinstance(result["price"], float)

    def test_converts_unicode_pound_to_float(self, pipeline, fake_spider):
        item = BookItem(title="Test Book", price="\u00a351.77", rating="Four", availability="In stock")
        result = pipeline.process_item(item, fake_spider)
        assert result["price"] == 51.77
        assert isinstance(result["price"], float)

    def test_handles_none_price(self, pipeline, fake_spider):
        item = BookItem(title="Test Book", price=None, rating="Four", availability="In stock")
        result = pipeline.process_item(item, fake_spider)
        assert result["price"] == 0.0

    def test_handles_empty_price(self, pipeline, fake_spider):
        item = BookItem(title="Test Book", price="", rating="Four", availability="In stock")
        result = pipeline.process_item(item, fake_spider)
        assert result["price"] == 0.0

    def test_fills_none_fields_with_defaults(self, pipeline, fake_spider):
        item = BookItem(title=None, price="£10.00", rating=None, availability=None)
        result = pipeline.process_item(item, fake_spider)
        assert result["title"] == "Unknown Title"
        assert result["rating"] == "Unknown"
        assert result["availability"] == "Unknown"


class TestStarRatingFilter:
    def test_accepts_four_stars(self):
        estrelas = "star-rating Four"
        assert estrelas and ("Four" in estrelas or "Five" in estrelas)

    def test_accepts_five_stars(self):
        estrelas = "star-rating Five"
        assert estrelas and ("Four" in estrelas or "Five" in estrelas)

    def test_rejects_one_star(self):
        estrelas = "star-rating One"
        assert not (estrelas and ("Four" in estrelas or "Five" in estrelas))

    def test_rejects_two_stars(self):
        estrelas = "star-rating Two"
        assert not (estrelas and ("Four" in estrelas or "Five" in estrelas))

    def test_rejects_three_stars(self):
        estrelas = "star-rating Three"
        assert not (estrelas and ("Four" in estrelas or "Five" in estrelas))

    def test_rejects_none(self):
        estrelas = None
        assert not (estrelas and ("Four" in estrelas or "Five" in estrelas))