from django.db import models

from usuario.models import Usuario
from livraria.models import Livro

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZAD0 = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras"
    )
    status = models.IntegerField(choices=StatusCompra.choices, default= StatusCompra.CARRINHO)

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="+")
    quantidade = models.IntegerField(default=1)