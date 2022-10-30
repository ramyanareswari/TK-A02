from django.shortcuts import render

def quiz_main_page(request):
    return render(request, 'quiz_main_page.html')

def show_questions(request):
    return render(request, 'questions.html')

def show_result(request):
    return render(request, 'result.html')