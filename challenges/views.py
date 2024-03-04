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
    "december":None,
}

# Create your views here.
def index(request):
    list_item =""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html", {
        "months": months
    })

def monthly_challenge_int(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("No such month")
    else:
        selected_month = months[month-1] # Must minus 1 as list index starts from 0
        redirected_path = reverse("monthly-challenge",args=[selected_month])
        return HttpResponseRedirect(redirected_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{'text':challenge, 'month_name': month})
    except:
        return HttpResponseNotFound("No such month. Please try again")