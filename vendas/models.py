from django.db import models


class Venda(models.Model):
    cliente = models.IntegerField()
    voo_ida = models.IntegerField()
    voo_volta = models.IntegerField()
    hotel = models.IntegerField()
    diarias = models.IntegerField()
    data_viagem = models.DateField()
    realizada_em = models.DateTimeField(auto_now_add=True)


class VendaComissao(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    comissao = models.DecimalField(
        max_digits=6, decimal_places=2, default=100.00)
