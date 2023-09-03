from django.shortcuts import render


# Home Page View
def home(request):
    return render(request, "home.html")


# Opportunities View
def opportunities(request):
    return render(request, "opportunities.html")
