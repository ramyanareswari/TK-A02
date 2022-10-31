
from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from tips.forms import AddArticle

from django.views.decorators.csrf import csrf_exempt


from tips.models import TipsArticle

# =============== Show all article =============== #
def show_tips_article(request):
    articles = TipsArticle.objects.all()
    data = []
    for obj in articles:
        item = {
            'pk': obj.id,
            'author': obj.author.username,
            'title': obj.title,
            'content': obj.content,
        }
        data.append(item)
    context = {
        'author': request.user.username,
        'articles': articles,
        'data':data,
        'form': AddArticle()
    }
    return render(request, 'tips.html', context)
    
    # return JsonResponse({'data':data})
    
    

# =============== Add article modal =============== #
@csrf_exempt
def add_article(request):

    form = AddArticle(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
            # author = request.author
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # save the form data to model
        art = form.save(commit=False)
        art.author = User.objects.get(username = request.user)
        art.save()
        
        # when saved json dump
        response = {
                'pk': art.id,
                'author': art.author.username,
                'title': art.title,
                'content': art.content,
                'publish': art.publish,
                'url' : '/articles'
                }

        return JsonResponse(response)
        

#  ==== AJAX view which returns a JSON object from json database ====
def get_article(request):
    tipsObj = TipsArticle.objects.filter(author = request.user)

    data = serializers.serialize('json', tipsObj)
    return HttpResponse(data, content_type="application/json")




# =============== Delete article =============== #

# =============== Like article =============== #

# =============== Sort article =============== #
