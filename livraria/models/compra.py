from django.db import models

from usuario.models import Usuario
from livraria.models import Livro

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZAD0 = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"
        
    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras"
    )
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    data = models.DateTimeField(auto_now_add=True, null=True)
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.CARTAO_CREDITO)
    
    @property
    def total(self):
     # total = 0
        # for item in self.itens.all():
        #     total += item.livro.preco * item.quantidade
        # return total
        return sum((item.preco_item or 0) * item.quantidade for item in self.itens.all())



class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
