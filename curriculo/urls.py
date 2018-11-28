from django.urls import path

from .views import curso, disciplina

app_name = 'curriculo'
urlpatterns = [
    path('<str:sigla>/', curso, name='curso'),
    path('<str:sigla>/disciplina/<str:identificador>/', disciplina, name="disciplina")
]