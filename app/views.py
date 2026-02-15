from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def konaba(request):
    return render(request, "konaba.html")

def membru(request):
    return render(request, "membru.html")