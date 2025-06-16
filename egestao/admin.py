from django.contrib import admin
from .models import Categoria, Produto, Movimentacao

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'categoria', 'preco', 'quantidade', 'estoque_minimo')
    list_filter = ('categoria',)
    search_fields = ('nome', 'codigo')

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data', 'usuario')
    list_filter = ('tipo', 'data')
    search_fields = ('produto__nome', 'produto__codigo')

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)