from rest_framework import serializers
from vendas.models import Venda, VendaComissao


class VendaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Venda


class VendaComissaoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VendaComissao
