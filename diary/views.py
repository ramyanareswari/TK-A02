from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='/login/')
def show_diary(request):
    context = {
        'user': request.user,
    }
    return render(request, 'diary.html', context)

@csrf_exempt
@login_required(login_url='/login/')
def create_log(request):
    val = True
    if request.method == 'POST':
        a = request.POST.get('is_finished')
        if a == "True":
            val = True
        elif a == "False":
            val = False
        print(a)
        foodname = request.POST.get('foodname')
        description = request.POST.get('description')
        date = request.POST.get('date')
        price = request.POST.get('price')

        # if habis = checked return true, if tidak habis return false
        log = Diary.objects.create(
            user=request.user,
            foodname=foodname,
            description=description,
            date=date,
            is_finished = val,
            price=price)
            
        return JsonResponse(
            {
                'pk': log.id,
                'fields': {
                    'title': log.foodname,
                    'description': log.description,
                    'date': log.date,
                    'is_finished': log.is_finished,
                    'price': log.price
                },
            },
            status=200,
        )

@login_required(login_url='/login/')
def get_diarylog_json(request):
    data = Diary.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def delete_log(request, pk):
    if Diary.objects.get(pk = pk).user == request.user:
        Diary.objects.filter(pk = pk).delete()
    return redirect('diary:show_diary')