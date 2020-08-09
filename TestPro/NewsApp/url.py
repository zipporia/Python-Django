from django.urls import path
from .views import NewsP, Home, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
]