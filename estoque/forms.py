from django import forms
from .models import ProdutoModel


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = ['codigo', 'nome', 'secao', 'qtde', 'contagem']