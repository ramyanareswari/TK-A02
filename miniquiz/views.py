from miniquiz.models import *
from django.shortcuts import render
from django.http import JsonResponse

# View main page to start quiz
def show_quiz_homepage(request):
    quiz = QuizModel.objects.all()
    return render(request, 'main.html', {'quizs' : quiz})

# View quiz page to start the quiz
def show_quiz_mainpage(request, pk):
    quiz = QuizModel.objects.get(pk = pk)
    return render(request, 'quiz.html', {'obj': quiz})

# View quiz questions and answers in json format
def show_quiz_json(request, pk):
    quiz = QuizModel.objects.get(pk = pk)
    questions = []

    for q in quiz.get_questions():
        answers = []

        for a in q.get_answers():
            answers.append(a.text)

        questions.append({str(q): answers})
    
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

# Save the quiz and view the result
def save_quiz(request, pk):
    
    if(request.is_ajax()):

        # State variables for accomodate question object
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        #data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        # Looping data.keys for getting question object
        for k in data_.keys():

            # Append question object to questions
            question = QuestionModel.objects.get(text=k)
            questions.append(question)

        # State variables for calculating score
        score = 0
        full_score = 0
        results = []
        correct_answer = None
        full = True

        # Looping questions
        for q in questions:

            # Get user answer
            a_selected = request.POST.get(q.text)

            # Executed when user answer the question
            if(a_selected != ""):
                
                # Question_answer is all answer for each question
                truth = False
                max_score = 0
                question_answer = AnswerModel.objects.filter(question=q)
                
                # Looping questions_answer
                for a in question_answer:
                    
                    # Check if question answer is equal with a.text and user haven't answer the question correctly
                    if a_selected == a.text and (not truth):
                        
                        # If a is correct answer, initialize correct_answer with a
                        if a.correct:
                            truth = True
                            correct_answer = a.text
                            results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})

                        # Add score with a.poin
                        score += a.point

                    # Executed if user anser not equal with a.text or user have answer the question correctly
                    else:

                        # If a corect, initialize correct_answer with a.text
                        if a.correct:
                            correct_answer = a.text


                    # Initialize max_score if a.poin is greater than max_score
                    if a.point > max_score :
                        max_score = a.point


                full_score += max_score

                # Executed if user haven't answer the question correctly
                if not truth:
                    results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})

            # Excecuted if user doesn't answer the question
            else:
                results.append({str(q): 'not-answered'})
                full = False

        # Get user object and quiz object
        user = request.user
        quiz = QuizModel.objects.get(pk=pk)

        # Executed if user full_score == 0
        if full_score!=0:
            score = round(score/full_score * 100, 2)
        
        # Executed if full_score != 0
        else :
            score = 0

        # If user answer all question, create Result onject and send data using JsonResponse
        if full:
            ResultModel.objects.create(quiz=quiz, user=user, final_score=score)

            if score >= quiz.required_score_to_pass:
                return JsonResponse({'quiz': quiz.name, 'passed': "True", 'score': score, 'results': results, 'full': "True"})
        
            else:
                return JsonResponse({'quiz': quiz.name, 'passed': "False", 'score': score, 'results': results, 'full': "True"})
        
        # If not, state full as false and send data
        else:
            return JsonResponse({'quiz': quiz.name, 'passed': "False", 'score': score, 'results': results, 'full': "False"})