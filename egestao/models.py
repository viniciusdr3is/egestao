from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"
    
    @property
    def estoque_baixo(self):
        return self.quantidade < self.estoque_minimo

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.get_tipo_display()} de {self.quantidade} {self.produto}"
    
    def clean(self):
        if self.tipo == 'S' and self.quantidade > self.produto.quantidade:
            raise ValidationError('Quantidade em estoque insuficiente.')
    
    def save(self, *args, **kwargs):
        # Atualiza o estoque do produto
        produto = self.produto
        if self.tipo == 'E':
            produto.quantidade += self.quantidade
        else:
            produto.quantidade -= self.quantidade
        produto.save()
        super().save(*args, **kwargs)