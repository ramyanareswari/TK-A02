from django.urls import path
from miniquiz.views import *

app_name = 'miniquiz'

urlpatterns = [
    path('', show_quiz_homepage, name='show_quiz_homepage'),
    path('start/', show_quiz_mainpage, name='show_quiz_mainpage'),
    path('data/', show_quiz_json, name='show_quiz_json'),
    path('save/', save_quiz, name='save_quiz'),
]