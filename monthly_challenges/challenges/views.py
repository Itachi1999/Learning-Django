from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": None,
}

challenge_text = ""

def index(request):
    months = list(monthly_challenges.keys())
    # list_items = ""

    # for month in months:
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href= {month_path}>{month.capitalize()}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"

    return render(request=request, template_name="challenges/index.html", context= {
        "months": months
    })

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > 0:
        try:
            forward_month = months[month - 1]
        except:
            response_data = render_to_string("404.html")
            return HttpResponseNotFound(response_data)
    else:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    return HttpResponseRedirect(forward_month)

def monthly_challenge(request, month):
    try: 
        challenge_text = monthly_challenges[month]
        return render(request=request, template_name="challenges/challenge.html",context={
            "text" : challenge_text,
            "month": month.capitalize(),
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
