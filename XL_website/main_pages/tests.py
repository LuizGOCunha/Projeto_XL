from django.test import TestCase, RequestFactory
from django.test import LiveServerTestCase
from selenium import webdriver

class XLTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/luiz/Projects/XL_clone/Projeto_XL/XL_website/main_pages/selenium/geckodriver')
        
    def tearDown(self):
        self.browser.quit()
    
    def test_para_verificar_se_o_site_está_abrindo(self):
        """Teste verifica se o site e suas rotas estão alcansáveis"""
        self.browser.get(self.live_server_url)
        self.browser.get(self.live_server_url + '/sobre')
        self.browser.get(self.live_server_url + '/contato')  
        self.browser.get(self.live_server_url + '/projetos')
           
        
  

    


#    def test_que_exemplifica_falha(self):
#        """Esse teste deve falhar obrigatoriamente"""
#        self.fail('Falha obrigatória, não se preocupe')

# Toda ver que executo o teste que verifica se as rotas estão alcansáveis, surge o seguinte erro:
"""File "/usr/lib/python3.8/posixpath.py", line 76, in join
    a = os.fspath(a)
TypeError: expected str, bytes or os.PathLike object, not NoneType""" 
# E isso só acontece quando me utilizo de self.live_server_url
# Mas os teste funcionam do mesmo jeito. Preciso descobrir o motivo depois.  

#                       *** RESOLVIDO!! *** 
# O problema era a falta de um STATIC_ROOT em settings.py
# Sempre lembrar de configurar ROOT e URL, nunca somente um!!

# ====================================================================================================    

# Além disso, toda vez que se tenta importar um módulo por dentro deste mesmo pacote (como 'views.py')
# se encontra o erro:
"""ModuleNotFoundError: No module named 'views'"""

#                       *** RESOLVIDO!! ***
# O problema era que eu não estava importando o views de acordo com boa prática
# Errado: from views import x, y, z
# Correto: from . import views
# Dessa forma se tem certeza onde o Django deve procurar.

