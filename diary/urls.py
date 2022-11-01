from django.urls import path
from diary.views import *

app_name = 'diary'

urlpatterns = [
    path('create-log/', create_log, name='create_log'),
    path('', show_diary, name='show_diary'),

]