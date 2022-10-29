from django.urls import path
from send_foodwaste.views import *

app_name = 'send_foodwaste'

urlpatterns = [
    path('', show_send_foodwaste, name='show_send_foodwaste'),
]