
from rest_framework.viewsets import ModelViewSet
from .models import Producto, Cliente, Venta
from .serializers import ProductoSerializer, ClienteSerializer, VentaSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


    
