from django.test import LiveServerTestCase
from selenium import webdriver


class LiveServerTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.maximize_window()
        cls.url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_setup_is_correct(self):
        self.selenium.get(self.url)
        self.assertEquals('Not Found', self.selenium.title)