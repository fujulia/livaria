from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from livraria.models import Compra, ItensCompra
from rest_framework import serializers

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade", "total"]
        depth = 2
     
        
    def get_total(self, instance):
        return instance.quantidade * (instance.livro.preco or 0)
        
class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    data = serializers.DateTimeField(read_only=True)
    tipo_pagamento = CharField(source="get_tipo_pagamento_display", read_only=True)
    
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens", "data", "tipo_pagamento")
    
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
        
    def validate(self, data):
        if data["quantidade"]> data["livro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponivel em estoque."}
            )
        return data
        
    
class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Compra
        fields = ("usuario", "itens")  
        
    def create(self, validated_data):
        itens= validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["livro"].preco
            ItensCompra.objects.create(compra=compra, **item)  
        compra.save()
        return compra
    
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                item["preco_item"] = item["livro"].preco
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance