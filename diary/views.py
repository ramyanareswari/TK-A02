from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers


@login_required(login_url='/login/')
def show_diary(request):
    context = {
        'user': request.user,
    }
    return render(request, 'diary.html', context)

@login_required(login_url='/login/')
def create_log(request):
    if request.method == 'POST':
        foodname = request.POST.get('foodname')
        description = request.POST.get('description')
        date = request.POST.get('date')
        log = Diary.objects.create(
            user=request.user,
            foodname=foodname,
            description=description,
            is_finished=False,
            date=date)
        return JsonResponse(
            {
                'pk': log.id,
                'fields': {
                    'title': log.foodname,
                    'description': log.description,
                    'is_finished': log.is_finished,
                    'date': log.date,
                },
            },
            status=200,
        )

def get_diarylog_json(request):
    diary = Diary.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", diary), content_type="application/json")
