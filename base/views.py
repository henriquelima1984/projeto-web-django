from django.shortcuts import render
from django.http import HttpResponse # noqa

# Create your views here.


def home(request):
    return render(request, 'base/home.html')
