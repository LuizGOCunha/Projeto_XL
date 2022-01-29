from django.test import TestCase, RequestFactory
from . import views



class XLTestCaseURLS(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        pass

    def test_para_saber_se_a_rota_principal_usa_o_template_correto(self):
        """Esse teste cria um objeto request para testar se o view index está utilizando o
           template de nome index.html"""
        request = self.factory.get('')
        with self.assertTemplateUsed('index.html'):
            response = views.index(request)
            self.assertEqual(response.status_code, 200)

    def test_para_saber_se_a_rota_contato_usa_o_template_correto(self):
        """Esse teste cria um objeto request para testar se o view contato está utilizando o
           template de nome contato.html"""
        request = self.factory.get('')
        with self.assertTemplateUsed('contato.html'):
            response = views.contato(request)
            self.assertEqual(response.status_code, 200)
    