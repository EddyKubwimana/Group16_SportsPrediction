from django import forms
from .models import  storageModel
from django.db import models

# class for model built to predict fifa overall rating
class fifaModel(forms.ModelForm):

   class Meta:
       model = storageModel
       fields = ["VALUE_EUR", "RELEASE_CLAUSE_EUR","AGE","POTENTIAL","MOVEMENT_REACTION","PREDICTION", "CONFIDENCE"]











