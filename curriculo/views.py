from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import Curso, DisciplinaOfertada, Disciplina

# Create your views here.
def curso(request, sigla):
    curso = get_object_or_404(Curso, sigla=sigla)

    curso.semestres = range(1, curso.duracao+1)

    hoje = datetime.now()
    ano = hoje.year
    semestre = 1 if hoje.month <=6 else 2    
    disciplinas_ofertadas = DisciplinaOfertada.objects.filter(curso=curso)

    disciplinas = []

    for do in disciplinas_ofertadas:
        disciplina = get_object_or_404(Disciplina, nome= do.disciplina.nome)
        setattr(disciplina,'semestre',do.semestre)
        disciplinas.sort(key=lambda disciplina: disciplina.semestre)
        if disciplina not in disciplinas:
            disciplinas.append(disciplina)
    context = {
        'curso': curso,
        'disciplinas': disciplinas
    }
    return render(request, 'curriculo/curso.html', context)

def disciplina(request, sigla, identificador):
    disciplina = Disciplina.objects.filter(identificador__iexact = identificador).first()
    context = {
        'disciplina':disciplina
    }
    return render(request, 'curriculo/disciplina.html', context)