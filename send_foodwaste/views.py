from django.shortcuts import render

# Create your views here.
def show_send_foodwaste(request):
    return render(request, 'send_foodwaste.html')