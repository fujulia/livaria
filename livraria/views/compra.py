from rest_framework.viewsets import ModelViewSet

from livraria.models import Compra 
from livraria.serializers import CompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer