# product/serializers.py

from rest_framework import serializers
from .models import Product, Category  # Certifique-se de que o modelo Category está no arquivo models.py

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
