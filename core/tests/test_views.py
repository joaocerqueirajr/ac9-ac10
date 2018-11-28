from django.test import SimpleTestCase
from django.urls import reverse

from django.contrib.messages import get_messages

class CoreViewsTest(SimpleTestCase):

    allow_database_queries = True

    def test_index_status_200(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'index.html')

    def test_index_status_200_pelo_nome(self):
        response = self.client.get(reverse("core:home"))
        self.assertTemplateUsed(response, 'index.html')

    def test_contato_status_200(self):
        response = self.client.get("/contato/")
        self.assertTemplateUsed(response, 'contato.html')

    def test_contato_status_200_pelo_nome(self):
        response = self.client.get(reverse("core:contato"))
        self.assertTemplateUsed(response, 'contato.html')

    def test_contato_post_invalido(self):
        response = self.client.post(reverse("core:contato"), {'email':'', 'nome':'', 'assunto':'', 'mensagem':''})
        self.assertEqual(response.context['mensagem'], 'Não foi possível enviar o seu e-mail, tente novamente mais tarde.')
        self.assertEqual(response.context['mensagem_tipo'], 'erro')