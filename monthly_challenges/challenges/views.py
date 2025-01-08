from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges= {
    "january":"study",
    "february":"study more",
    "march":"ramadan and annas birthday",
    "april": "more studying",
    "may":"moremore may ",
    "june":"june june",
    "july":"birhtday",
}
# Create your views here.
def index(request):
     
     list_items = ""
     months = list(monthly_challenges.keys())
     for month in months:
          month_path = reverse("month-challenge", args=[month])
          list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
     response_data = f"<ul>{list_items}</ul>"
     months=[]
     for month in monthly_challenges:
          months.append(month)
          
     return HttpResponse(f"<ul>{list_items}</ul>")
def monthly_challenge_number(request, month):
        months = list(monthly_challenges.keys())
        forward_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)