from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
]