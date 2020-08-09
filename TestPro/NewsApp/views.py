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




def Contact(request):
    return render(request, 'contact.html')