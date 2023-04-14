from django.urls import path
from hello import views
from .views import *

urlpatterns = [
    path("",views.home, name="home"),
    path("api/get/", api , name="api")
]