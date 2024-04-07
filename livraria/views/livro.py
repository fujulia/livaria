from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro

from livraria.serializers import LivroSerializer, LivroListSerializer, LivroDetailSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao", "editora__nome"]
    search_fields = ["titulo"]
    ordering_fields = ["titulo", "preco"]
    ordering = ["titulo"]
    
def get_serializer_class(self):
    if self.action == "list":
        return LivroListSerializer
    elif self.action == "retrieve":
        return LivroDetailSerializer
    return LivroSerializer
