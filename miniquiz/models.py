from django.db import models

class miniQuiz(models.Model):
    questions = models.CharField(max_length=100)