from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

challenge_text = ""

def index(request, month):
    if month == "january":
        challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    else:
        return HttpResponseNotFound("Not a month")
    return HttpResponse(challenge_text)
