from django.shortcuts import render


def home(request):
    return render(request,"recipes/home.html")

def sobre(request):
    return HttpResponse("Sobre") 

def contato(request):
    return render(request, "recipes/contato.html")

