from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Produto, Movimentacao
from .forms import ProdutoForm, MovimentacaoForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

@login_required
def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'form_produto.html', {'form': form, 'titulo': 'Novo Produto'})

@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'form_produto.html', {'form': form, 'titulo': 'Editar Produto'})

@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'confirmar_exclusao.html', {'obj': produto})

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    return render(request, 'lista_movimentacoes.html', {'movimentacoes': movimentacoes})

@login_required
def nova_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST, user=request.user)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.usuario = request.user
            movimentacao.save()
            return redirect('lista_movimentacoes')
    else:
        form = MovimentacaoForm(user=request.user)
    return render(request, 'form_movimentacao.html', {'form': form, 'titulo': 'Nova Movimentação'})

def estoque_baixo(request):
    # Filtrar produtos com estoque baixo e calcular a diferença
    produtos = Produto.objects.filter(quantidade__lt=models.F('estoque_minimo'))
    
    # Adicionar a diferença calculada para cada produto
    for produto in produtos:
        produto.diferenca = produto.quantidade - produto.estoque_minimo
    
    return render(request, 'estoque_baixo.html', {'produtos': produtos})

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')