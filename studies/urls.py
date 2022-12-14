from django.urls import path
from . import views

app_name = "studies"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create_todos/<int:study_pk>", views.create_todos, name="create_todos"),
    path(
        "detail/<int:study_pk>/<int:management_pk>",
        views.delete_todos,
        name="delete_todos",
    ),
    path("detail/<int:study_pk>", views.detail, name="detail"),
    path("detail/<int:study_pk>/delete", views.delete, name="delete"),
    path("detail/<int:study_pk>/update", views.update, name="update"),
    path("info/<int:study_pk>", views.info, name="info"),
    path("detail/<int:study_pk>/join", views.join, name="join"),
    path("detail/<int:study_pk>/<int:user_pk>/refusal", views.refusal, name="refusal"),
    path(
        "detail/<int:study_pk>/<int:user_pk>/accept_and_drive_out",
        views.accept_and_drive_out,
        name="accept_and_drive_out",
    ),
]
