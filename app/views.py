from rest_framework import generics
from .models import Seller, Product,Category
from .serializers import SellerSerializer, ProductSerializer,CategorySerializer,ProductMainSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SellerDetailView(generics.RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = "id"  

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SellerProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        seller_id = self.kwargs['seller_id']
        return Product.objects.filter(seller_id=seller_id)
    
class CatogoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductMainWindowApi(generics.ListAPIView):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductMainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at']
    
