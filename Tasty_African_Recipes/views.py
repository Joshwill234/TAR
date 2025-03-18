from django.shortcuts import render

def home(request):
    return render(request, "Tasty_African_Recipes/home.html")

def signup(request):
    return render(request, "Tasty_African_Recipes/signup.html")

def login(request):    
    return render(request, "Tasty_African_Recipes/login.html")

def blog(request):
    return render(request, "Tasty_African_Recipes/blog.html")

def search(request):
    return render(request, "Tasty_African_Recipes/search.html")