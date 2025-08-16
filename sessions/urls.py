from django.urls import path
from . import views

app_name = "sessions"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
    path("logout/", views.logout, name="logout"),
]