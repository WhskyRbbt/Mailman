from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import SignUpForm



# Landing route
def landing(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, '../templates/registration/login.html')

# def registration(request):
#     return render(request, 'registration/registration.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    return render(request, 'main_app/home.html')

def shipment(request):
    return render(request, 'main_app/newshipment.html')

def create_shipment(request):
    print("made it")

def profile(request):
    return render(request, 'main_app/profile.html')
