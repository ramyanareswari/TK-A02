from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quiz_homepage(request):
    return render(request, 'index.html')
