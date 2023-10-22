from django.db import models
from django.utils import timezone
# model for storing previous prediction entries for prediction

class storageModel(models.Model):

    DATE = models.DateTimeField(default = timezone.now)
    VALUE_EUR = models.FloatField(verbose_name= "VALUE EUR", default=0)
    RELEASE_CLAUSE_EUR = models.FloatField(verbose_name="RELEASE CLAUSE EUR", default=0)
    AGE = models.IntegerField(verbose_name= "AGE", default=0)
    POTENTIAL = models.FloatField(verbose_name="POTENTIAL", default=0)
    MOVEMENT_REACTION = models.FloatField(verbose_name = "MOVEMENT REACTION", default=0)
    PREDICTION = models.FloatField( default = 0,verbose_name= "PREDICTION", blank= True)
    CONFIDENCE = models.FloatField( default =0, verbose_name="CONFIDENCE", blank= True)

    def __str__self():

        return "Prediction"


