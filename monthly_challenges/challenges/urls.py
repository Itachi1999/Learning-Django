from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name='index'),
    path("<int:month>", view=views.monthly_challenge_number),
    path("<str:month>", view=views.monthly_challenge, name='month-challenge'),
]