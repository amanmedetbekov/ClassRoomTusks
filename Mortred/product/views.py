from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

