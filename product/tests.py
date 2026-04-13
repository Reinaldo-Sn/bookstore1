from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()

    def test_contains_expected_fields(self):
        data = CategorySerializer(self.category).data
        self.assertEqual(set(data.keys()), {"title", "slug", "description", "active"})

    def test_title_field_content(self):
        data = CategorySerializer(self.category).data
        self.assertEqual(data["title"], self.category.title)

    def test_active_field_content(self):
        data = CategorySerializer(self.category).data
        self.assertEqual(data["active"], self.category.active)


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=[self.category])

    def test_contains_expected_fields(self):
        data = ProductSerializer(self.product).data
        self.assertEqual(
            set(data.keys()), {"title", "description", "price", "active", "category"}
        )

    def test_title_field_content(self):
        data = ProductSerializer(self.product).data
        self.assertEqual(data["title"], self.product.title)

    def test_price_field_content(self):
        data = ProductSerializer(self.product).data
        self.assertEqual(data["price"], self.product.price)

    def test_category_is_nested(self):
        data = ProductSerializer(self.product).data
        self.assertEqual(len(data["category"]), 1)
        self.assertEqual(data["category"][0]["title"], self.category.title)
