from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContatoForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def contato(request):
    context = {}
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Sua mensagem foi enviada com sucesso') 
        else:
            messages.error(request, 'Problemas ao enviar seu e-mail!')
    else:
        form = ContatoForm()

    context["form"] = form
    return render(request, 'contato.html', context)

def error404(request, exception=None):
    return render(request, 'error/404.html')

def sair(request):
    logout(request)
    return redirect('core:home')

def entrar(request):
    context = {}
    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(username=usuario, password=senha)
        if usuario:
            login(request, usuario)
            if usuario.tipo == 'P':
                return redirect('restrito:home_professor')
            elif usuario.tipo == 'C':
                return redirect('restrito:home_coordenador')
            elif usuario.tipo == 'A':
                return redirect('restrito:home_aluno')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    return render(request, 'entrar.html', context)