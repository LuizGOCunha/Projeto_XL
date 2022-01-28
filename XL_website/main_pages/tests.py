import os
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver



class XLTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/luiz/Projects/XL_clone/Projeto_XL/XL_website/main_pages/selenium/geckodriver')


    def tearDown(self):
        self.browser.quit()

    
    def test_para_verificar_a_janela_do_browser(self):
        self.browser.get('localhost:8000')


# Create your tests here.
