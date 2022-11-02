import datetime
from homepage.models import ContactForm
from homepage.forms import CreateUserForm, FormContact
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

@csrf_exempt
def show_homepage(request):
    if request.method == 'POST': 
        form = FormContact(request.POST)
        data = {}
        print(request.POST)
        if form.is_valid():
            form.save()
            data['success'] = True
            print("Bismillah masuk ga3")
            return JsonResponse(data)
        else:
            data['success'] = False
            return JsonResponse(data)
    else:
        form = FormContact()
        return render(request, 'homepage.html', {'form':form})

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Selamat, akun '+ user +' berhasil dibuat. Silakan login!')
            return redirect('homepage:login')
        else:
            messages.info(request, "Input tidak valid")
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:show_homepage'))
    response.delete_cookie('last_login')
    return response
