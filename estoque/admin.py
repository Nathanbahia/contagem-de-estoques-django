from django.contrib import admin
from .models import ProdutoModel


@admin.register(ProdutoModel)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'secao', 'qtde', 'atualizacao')