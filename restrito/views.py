from django.shortcuts import render,get_object_or_404

from django.contrib.auth.decorators import login_required, user_passes_test

from contas.models import  Usuario, Aluno, Professor, Coordenador

def testa_professor(usuario):
    return usuario.tipo == 'P'


def testa_coordenador(usuario):
    return usuario.tipo == 'C'


def testa_aluno(usuario):
    return usuario.tipo == 'A'


@login_required
@user_passes_test(testa_professor)
def home_professor(request):
    user = get_user(request)
    context={
        'usuario':user
    }
    return render(request, 'restrito/home.html',context)

@login_required
@user_passes_test(testa_aluno)
def home_aluno(request):
    user = get_user(request)
    context={
        'usuario':user
    }
    return render(request, 'restrito/home.html',context)

@login_required
@user_passes_test(testa_coordenador)
def home_coordenador(request):
    user = get_user(request)
    context={
        'usuario':user
    }
    return render(request, 'restrito/home.html',context)
 
def get_user(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Usuario,username=request.user.username)
        if request.user.tipo == "P":
            return Professor.objects.filter(usuario=user).first()
        elif request.user.tipo == "A":
            return Aluno.objects.filter(usuario=user).first()
        elif request.user.tipo == "C":
            coord= Coordenador.objects.filter(usuario=user).first()
            return coord
        else:
            return None
    else:
        return None