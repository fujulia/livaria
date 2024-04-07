from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from livraria.models import Categoria

from livraria.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["descricao"]
    search_fields = ["descricao"]
    ordering_fields = ["descricao"]
    ordering =["descricao"]
    # permission_classes = [IsAuthenticated]