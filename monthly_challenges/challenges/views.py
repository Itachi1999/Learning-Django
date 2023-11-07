from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
eat = "Eat 3 meals everyday"
learn = "Learn new things for 20 mins everyday"
walk = "Walk for 20 mins every day"

monthly_challenges = {
    "january": eat,
    "february": learn,
    "march": walk,
    "april": walk,
    "may": learn,
    "june": eat,
    "july": learn,
    "august": walk,
    "september": eat,
    "october": learn,
    "november": eat,
    "december": walk,
}

challenge_text = ""

def monthly_challenge(request, month):
    try: 
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Not a supported month")
    return HttpResponse(challenge_text)
