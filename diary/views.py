from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import datetime
from django.core import serializers

# def show_diary(request):
#     context = {
#         'user': request.user,
#     }
#     return render(request, 'diary.html', context)

# # Create your views here.
# def create_log(request):
#     if request.method == 'POST':
#         foodname = request.POST.get('foodname')
#         description = request.POST.get('description')
#         log = Diary.objects.create(
#             user=request.user,
#             foodname=foodname,
#             description=description,
#             is_finished=False,
#             date=datetime.datetime.now())
#         return JsonResponse(
#             {
#                 'pk': log.id,
#                 'fields': {
#                     'title': log.foodname,
#                     'description': log.description,
#                     'is_finished': log.is_finished,
#                     'date': log.date,
#                 },
#             },
#             status=200,
#         )

# def get_diary_json(request):
#     diary = Diary.objects.filter(user=request.user)
#     return HttpResponse(serializers.serialize("json", diary), content_type="application/json")
