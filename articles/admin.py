from django.contrib import admin
from .models import Article  # imports from models.py file.

# Register your models here.

admin.site.register(Article)  # creates the Articles session in Django Admin, after importing the model for it.
