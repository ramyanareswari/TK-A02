from django.urls import path
from miniquiz.views import index

app_name = 'miniquiz'

urlpatterns = [
    path('', index, name='index'),
]