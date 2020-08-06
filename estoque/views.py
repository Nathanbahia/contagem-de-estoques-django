from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ProdutoModelForm
from .models import ProdutoModel
from django.contrib import messages


class IndexView(FormView):
    template_name = "index.html"
    form_class = ProdutoModelForm
    success_url = reverse_lazy("index")


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


    def form_valid(self, form):
        cod = form.cleaned_data['codigo']
        produto = ProdutoModel.objects.filter(codigo=cod).first()
        if produto is None:
            form.save()
        else:
            quantidade = form.cleaned_data['contagem']
            produto.contagem += float(quantidade)
            produto.save()
            messages.success(self.request, f'Produto atuzalizado com sucesso:\n{produto.nome} ')
        return super(IndexView, self).form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar produto.')
        return super(IndexView, self).form_invalid(form)
