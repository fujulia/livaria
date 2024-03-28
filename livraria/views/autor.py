from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor

from livraria.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
