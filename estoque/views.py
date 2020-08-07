from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ProdutoModelForm
from .models import ProdutoModel
from django.shortcuts import render

def index(request):
    form = ProdutoModelForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            cod = form.cleaned_data['codigo']
            produto = ProdutoModel.objects.filter(codigo=cod).first()
            quantidade = form.cleaned_data['contagem']

            if produto is None:
                form.save()
                estoque = quantidade

            else:
                produto.contagem += float(quantidade)
                estoque = produto.contagem
                produto.save()

            context = {'produto': produto, 'codigo': cod, 'quantidade': quantidade, 'estoque': estoque}

        else:
            context = {'produto': 'Erro', 'codigo': 'Erro', 'quantidade': 'Erro', 'estoque': 'Erro'}

    return render(request, 'index.html', context)