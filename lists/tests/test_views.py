from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from lists.views import ToDoListView

import pprint

pp = pprint.PrettyPrinter(indent=2)
User = get_user_model()


class ToDoListViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='test',
            email='test@email.com',
        )

    @classmethod
    def setUpClass(cls):
        cls.request_factory = RequestFactory()
        cls.url = '/to-do/list/'
        super().setUpClass()

    def test_authentication_required(self):
        request = self.request_factory.get(self.url)
        request.user = AnonymousUser()

        response = ToDoListView.as_view()(request)

        self.assertEqual(302, response.status_code)
        self.assertEqual(
            f'/accounts/login/?next={self.url}',
            response.headers['Location']
        )

    def test_valid_page_renders_on_GET(self):
        request = self.request_factory.get(self.url)
        request.user = self.user

        response = ToDoListView.as_view()(request)

        self.assertEqual(200, response.status_code)
        self.assertEqual(['lists/lists.html'], response.template_name)
