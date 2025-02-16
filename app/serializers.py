from rest_framework import serializers
from .models import Seller, Product, Category

class SellerSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    sold_products_count = serializers.IntegerField(source='sold', read_only=True)
    
    class Meta:
        model = Seller
        fields = ['id', 'full_name', 'image', 'backgroud_image', 'sold_products_count', 'income', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']

class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'seller', 'category', 'title', 'price', 'pages', 'file_size', 'file_type', 'file']

class ProductMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'created_at','poster']
        