from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.detail, name="detail"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/comments", views.create, name="create_comment"),
    path("<int:id>/comments/delete", views.delete_comment, name="delete_comment"),
    path("new/", views.new, name="new"),
]
