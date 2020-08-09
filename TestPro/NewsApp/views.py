from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News

# Create your views here.


def Home(request):

    context = {
        "name": "Mark Corn",
        "number": 254
    }

    return render(request, 'home.html', context)


def NewsP(request):
    obj = News.objects.get(id=1)

    context = {
        "data": obj
    }

    return render(request, 'new.html', context)


def NewsDate(request, year):

    article_list = News.objects.filter(pub_date_year=year)

    context = {
        'year': year,
        'article_list': article_list
    }

    return render(request, 'newsdate.html', context)


def Contact(request):
    return render(request, 'contact.html')