from django.urls import path
from miniquiz.views import *

app_name = 'miniquiz'

urlpatterns = [
    path('', quiz_main_page, name='quiz_main_page'),
    path('questions/', show_questions, name='show_questions'),
    path('result/', show_result, name='show_result'),
]