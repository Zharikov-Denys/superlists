from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from seleniumlogin import force_login

from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint


pp = pprint.PrettyPrinter(indent=2)
User = get_user_model()


class ToDoListPageLiveServerTests(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@email.com',
            password='testpass123',
        )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.maximize_window()

        cls.url = reverse('to_do_list')
        cls.full_url = cls.live_server_url + cls.url

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def tearDown(self):
        self.selenium.refresh()

    def test_authentication_required(self):
        self.selenium.get(self.full_url)

        self.assertEqual(
            f'{self.live_server_url}/accounts/login/?next={self.url}',
            self.selenium.current_url
        )

    def test_page_title(self):
        force_login(self.user, self.selenium, self.live_server_url)

        self.selenium.get(self.full_url)

        self.assertEqual('Your To-Do list', self.selenium.title)
