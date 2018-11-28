from django.test import TestCase
from django.conf import settings


class CoreAppTest(TestCase):

    def test_application_installed(self):
        installed = False
        for app in settings.INSTALLED_APPS:
            if app == 'core':
                installed = True
                break
        self.assertTrue(installed,msg="Não foi encontrada a aplicação core instalada (maiúsculas e minúsculas fazem diferença)")

    def test_urls_namespace(self):
        
        try:
            from core.urls import app_name
        except ImportError:
            self.fail('Não foi encontrado o módulo URLS dentro do core')
        self.assertEqual(app_name, 'core', msg="Namepsace 'core' não foi registrado nas url's")