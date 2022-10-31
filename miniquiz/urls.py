from django.urls import path
from miniquiz.views import *

app_name = 'miniquiz'

urlpatterns = [
    path('', show_mainpage, name='show_mainpage'),
    path('start/', show_quiz, name='show_quiz'),
    path('data/', show_quiz_json, name='show_quiz_json'),
    path('save/', save_quiz, name='save_quiz'),
]