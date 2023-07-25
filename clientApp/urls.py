from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("nurses",views.nurses, name="nurses"),

]