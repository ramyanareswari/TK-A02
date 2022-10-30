from audioop import add
from django.urls import path
from tips.views import show_tips_article, add_article, get_article

app_name = 'tips'

urlpatterns = [
    path('', show_tips_article, name='show_article'),
    path('articles/add-article/', add_article, name='add_article'),
    path('articles/get-article/', get_article, name='get_article')
]
