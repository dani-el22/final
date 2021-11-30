from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "green"

urlpatterns = [
    path("",views.home, name="home.html"),
    path("signup/",views.home, name="home.html")
]
