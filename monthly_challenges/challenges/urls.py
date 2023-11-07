from django.urls import path
from . import views

urlpatterns = [
    path("<month>", view=views.index),
]