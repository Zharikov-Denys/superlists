from django.test import TestCase
from django.urls import reverse, resolve

from lists.views import ToDoListView

import pprint

pp = pprint.PrettyPrinter(indent=2)


class UrlsTests(TestCase):
    
    def test_to_do_list_page_url_name_existence(self):
        url = reverse('to_do_list')
        self.assertEqual('/to-do/list/', url)
    
    def test_to_do_list_page_returns_correct_view(self):
        url = reverse('to_do_list')
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, ToDoListView.as_view().__name__)

