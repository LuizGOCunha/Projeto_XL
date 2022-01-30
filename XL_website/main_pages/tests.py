from dis import Bytecode
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

    def test_para_verificar_o_texto_do_site(self):
        """Esse teste verifica se os textos da página principal estão corretos"""
        self.browser.get(self.live_server_url)
        titulo = self.browser.find_element_by_css_selector('h1')
        lema = self.browser.find_element_by_css_selector('.navbar-text')
        self.assertEqual('Sobre a empresa', titulo.text)
        self.assertEqual('Dia a dia construindo o Ceará', lema.text)

    def test_para_verificar_se_os_botoes_estao_corretos(self):
        """Esse teste verifica se os nossos botões tem o texto correto e se seus links carregam"""
        self.browser.get(self.live_server_url)
        home = self.browser.find_element_by_css_selector('#botao_home')
        sobre = self.browser.find_element_by_css_selector('#botao_sobre')
        projetos = self.browser.find_element_by_css_selector('#botao_projetos')
        contato = self.browser.find_element_by_css_selector('#botao_contato')
        self.assertEqual(home.text, 'Página principal')
        self.assertEqual(sobre.text, 'Sobre Nós')
        self.assertEqual(projetos.text, 'Projetos')
        self.assertEqual(contato.text, 'Contatos')
        home.click()
        self.browser.find_element_by_css_selector('#botao_sobre').click()
        self.browser.find_element_by_css_selector('#botao_projetos').click()
        self.browser.find_element_by_css_selector('#botao_contato').click()
        # Você pode me perguntar "Você reutilizou o elemento home, por que não reutilizou os outros?"
        # A resposta é simples:
        # Quando você busca o primeiro link (home), ele está utilizável, mas no momento em que se vai para
        # outra página, todos os outros links anteriores se perdem, diante do fato de que atualizamos
        # o endereço.
        # Por isso, ao invés de tentarmos puxar um elemento anteriormente encontrado e agora perdido (O que
        # ergueria uma excessão), simplesmente pedimos para o selenium procurar um novo elemento na nova
        # página.

        

        

        
           
        
  

    


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

