from django.urls import path

from .views import index, contato, entrar, sair

app_name = "core"

urlpatterns = [
    path("", index, name="home"),
    path('contato/', contato, name="contato"),
    path('entrar/', entrar, name="login"),
    path('sair/', sair, name="logout")
]