from django.urls import path
from . import views
from .views import (
    HomeView,
    home,
    lista_produtos,
    novo_produto,
    editar_produto,
    excluir_produto,
    lista_movimentacoes,
    nova_movimentacao,
    estoque_baixo,
    CustomLoginView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # URLs de Produtos
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/novo/', novo_produto, name='novo_produto'),
    path('produtos/editar/<int:pk>/', editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
    
    # URLs de Movimentações
    path('movimentacoes/', lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/nova/', nova_movimentacao, name='nova_movimentacao'),

    # URLs de Estoque Baixo
    path('estoquebaixo/', estoque_baixo, name='estoque_baixo')
]