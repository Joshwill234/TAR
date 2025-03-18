from django.shortcuts import render

def index(request):
    return render(request, "Tasty_African_Recipes/index.html")

