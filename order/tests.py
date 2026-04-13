from django.test import TestCase

from order.factories import OrderFactory, UserFactory
from order.serializers.orde_serializer import OrderSerializer
from product.factories import CategoryFactory, ProductFactory


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=[self.category])
        self.user = UserFactory()
        self.order = OrderFactory(user=self.user, product=[self.product])

    def test_contains_expected_fields(self):
        data = OrderSerializer(self.order).data
        self.assertEqual(set(data.keys()), {"product", "total"})

    def test_product_is_nested(self):
        data = OrderSerializer(self.order).data
        self.assertEqual(len(data["product"]), 1)
        self.assertEqual(data["product"][0]["title"], self.product.title)

    def test_total_equals_sum_of_product_prices(self):
        data = OrderSerializer(self.order).data
        self.assertEqual(data["total"], self.product.price)

    def test_total_with_multiple_products(self):
        product2 = ProductFactory(category=[self.category])
        self.order.product.add(product2)
        data = OrderSerializer(self.order).data
        self.assertEqual(data["total"], self.product.price + product2.price)
