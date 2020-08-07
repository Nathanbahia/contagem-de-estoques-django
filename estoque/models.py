from django.db import models


class ProdutoModel(models.Model):
    codigo = models.CharField('Código', max_length=15)
    nome = models.CharField('Nome', max_length=100)
    secao = models.CharField('Seção', max_length=60)
    qtde = models.FloatField('Quantidade')
    contagem = models.FloatField('Contagem')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
