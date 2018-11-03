from vendas.models import VendaComissao, Venda
from vendas.serializers import VendaComissaoSerializer, VendaSerializer
from rest_framework import generics


class VendaComissaoListar(generics.ListAPIView):
    queryset = VendaComissao.objects.all()
    serializer_class = VendaComissaoSerializer


class VendaCriarListar(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class VendaDetalheApagar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
