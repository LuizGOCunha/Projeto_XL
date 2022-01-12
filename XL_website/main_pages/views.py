from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def projetos(request):
    return render(request, 'projetos.html')


def contato(request):
    return render(request, 'contato.html')