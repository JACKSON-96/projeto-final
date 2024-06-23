# order/serializers.py

from rest_framework import serializers
from order.models import Order
from product.models import Product  # Adicione esta linha para importar a classe Product
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        order = Order.objects.create(**validated_data)
        for product in product_data:
            order.product.add(product)
        return order
