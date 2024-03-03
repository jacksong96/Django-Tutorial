from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january":"jan",
    "february":"feb",
    "march":"mar",
    "april":"apr",
    "may":"may",
    "june":"jun",
    "july":"jul",
    "august":"aug",
    "september":"sep",
    "october":"oct",
    "november":"nov",
    "december":"dec",
}

# Create your views here.
def index(request):
    list_item =""
    months = list(monthly_challenges.keys())
    for month in months:
        directed_path = reverse("monthly-challenge",args=[month])
        list_item += f"<li><a href='{directed_path}'>{month.capitalize()}</a></li>"
    response = f"<ul>{list_item}</ul>"
    return HttpResponse(response)

def monthly_challenge_int(request, monthly):
    months = list(monthly_challenges.keys())
    if monthly > len(months):
        return HttpResponseNotFound("No such month")
    else:
        selected_month = months[monthly-1] # Must minus 1 as list index starts from 0
        redirected_path = reverse("monthly-challenge",args=[selected_month])
        return HttpResponseRedirect(redirected_path)


def monthly_challenge(request, monthly):
    try:
        challenge = monthly_challenges[monthly]
        return render(request,"challenges/challenge.html",{'text':challenge, 'month': monthly.capitalize()})
    except:
        return HttpResponseNotFound("No such month. Please try again")