from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def Home(request):

    context = {
        "name": "Mark Corn",
        "number": 254
    }

    return render(request, 'home.html', context)


def News(request):

    context = {
        "list": ['Java', 'Python', 'C#', 'PHP', 'Javascript', 'C++'],
        "my_num": 45
    }

    return render(request, 'new.html', context)




def Contact(request):
    return render(request, 'contact.html')