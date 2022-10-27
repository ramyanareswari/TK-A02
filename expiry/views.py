from expiry.models import Food_Data
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='auth/login/')
def show_expiry(request):
    food_data = Food_Data.objects.filter(user = request.user).order_by('-food_expired_date')
    context = {
        'query_set_food': food_data,
        'username': request.user,
    }
    return render(request, "expiry.html", context)

@csrf_exempt
@login_required(login_url='auth/login/')
def add_food(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_expired_date = request.POST.get('food_expired_date')
        food = Food_Data.objects.create(user = request.user, food_name = food_name, food_expired_date = food_expired_date)
        return JsonResponse(
            {
                'pk': food.id,
                'fields': {
                    'food_name': food.food_name,
                    'food_expired_date': food.food_expired_date
                },
            },
            status=200,
        )

@login_required(login_url='auth/login/')
def delete_food(request, id):
    foods = Food_Data.objects.get(user = request.user, id = id)
    foods.delete()
    return JsonResponse(status = 200)
    # return redirect('expiry:show_expiry')

@login_required(login_url='auth/login/')
def show_json(request):
    foods = Food_Data.objects.filter(user = request.user).order_by('-food_expired_date')
    return HttpResponse(serializers.serialize("json", foods), content_type="application/json")