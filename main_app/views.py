from django.shortcuts import render

# Landing route
def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, "main_app/home.html")

def login(request):
    return render(request, 'registration/login.html')