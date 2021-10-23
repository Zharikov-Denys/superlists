from django.urls import path

from .views import ToDoListView


urlpatterns = [
    path('list/', ToDoListView.as_view(), name='to_do_list'),
]
