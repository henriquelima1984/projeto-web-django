from django.shortcuts import render
from django.http import HttpResponse # noqa

# Create your views here.
from modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
