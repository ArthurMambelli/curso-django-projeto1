from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse("Sobre a Laurinha Fofinha")


def contato(request):
    return HttpResponse("Contato da Laurinha Perfeita")