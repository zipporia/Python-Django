from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def News(request):
    return render(request, 'new.html')


def Contact(request):
    return render(request, 'contact.html')