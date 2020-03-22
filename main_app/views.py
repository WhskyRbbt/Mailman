from django.shortcuts import render

# Landing route
def landing(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, '../templates/registration/login.html')

def show_signup(request):
    return render(request, 'registration/signup.html')

def signup(request):
    print("made it")

def home(request):
    return render(request, 'main_app/home.html')

def shipment(request):
    return render(request, 'main_app/newshipment.html')

def create_shipment(request):
    print("made it")

def profile(request):
    return render(request, 'main_app/profile.html')
