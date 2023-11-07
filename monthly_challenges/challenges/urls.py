from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>", view=views.monthly_challenge),
]