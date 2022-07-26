from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("greet", views.greet, name="Greet"),
#    path("mean", views.mean, name="Mean"),
    path("mern", views.mern, name="Mern"),
]

