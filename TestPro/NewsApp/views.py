from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def Home(request):
    return HttpResponse("<h1>Home page</h1>")


def News(request):
    return HttpResponse("<h1>Latest News</h1>")


def Contact(request):
    return HttpResponse("<h1>Contact page</h1>")