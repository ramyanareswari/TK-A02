import email
from unicodedata import name
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()