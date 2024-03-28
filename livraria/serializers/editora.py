from rest_framework.serializers import ModelSerializer

from livraria.models import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
