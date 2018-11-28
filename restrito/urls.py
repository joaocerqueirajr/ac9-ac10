from django.urls import path

from .views import *

app_name = 'restrito'
urlpatterns = [
    path('coordenador/', home_coordenador, name="home_coordenador"),
    path('professor/', home_professor, name="home_professor"),
    path('aluno/', home_aluno, name="home_aluno"),

]