from django.shortcuts import render


# Create your views here.
def home(request):
    cities = ["Memphis", "Los Angeles", "Seattle", "Washington D.C.", "Orlando"]
    context = {"cities": cities}
    return render(request, "cities/home.html", context)
