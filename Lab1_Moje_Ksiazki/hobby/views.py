from django.shortcuts import render

def home(request):
    return render(request, 'hobby/home.html')

def gatunki(request):
    return render(request, 'hobby/gatunki.html')

def polecane(request):
    return render(request, 'hobby/polecane.html')

def kontakt(request):
    return render(request, 'hobby/kontakt.html')