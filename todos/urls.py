from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("today/", views.today, name="today"),
    path("create/", views.create, name="create"),
    path("delete/<int:todos_pk>", views.delete, name="delete"),
    path("week/<str:few_week>", views.week, name="week"),
    path("read_all", views.read_all, name="read_all"),
    path("update/<int:pk>", views.update, name="update"),
    path("test/stuty_list", views.stuty_list, name="stuty_list"),
]
