from django.shortcuts import render

# Create your views here.


def sobre(request):
    return render(request, 'sobre.html')


def projetos(request):
    return render(request, 'projetos.html')


def contato(request):
    return render(request, 'contato.html')