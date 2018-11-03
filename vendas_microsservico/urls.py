from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from vendas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comissoes/', views.VendaComissaoListar.as_view()),
    path('vendas/', views.VendaCriarListar.as_view()),
    path('vendas/<int:pk>/', views.VendaDetalheApagar.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
