from django.test import LiveServerTestCase
from selenium import webdriver


class HomePageLiveServerTests(LiveServerTestCase):

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

    def tearDown(self):
        self.selenium.refresh()

    def test_page_title(self):
        self.selenium.get(self.url)
        self.assertEqual('Your To-Do list', self.selenium.title)
