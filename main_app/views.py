from django.http import HttpResponse
from django.shortcuts import render

# Landing route
def landing(request):
    return render(request, 'landing.html')