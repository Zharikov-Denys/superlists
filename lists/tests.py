from django.test import LiveServerTestCase
from selenium import webdriver


class LiveServerTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_setup_is_correct(self):
        self.selenium.get('http://localhost:8000/')
        self.assertEquals('Page not found at /', self.selenium.title)
