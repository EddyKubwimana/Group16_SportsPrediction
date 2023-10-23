from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import fifaModel
from .models import storageModel
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import joblib 
import os
import numpy as np
import pandas as pd

def prediction(request):
    
    # path to the model path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "votingpremium.joblib")
    SCALER_PATH = os.path.join(os.path.dirname(__file__), "scalerpremium.joblib")
    template_name = 'user/model.html'

    if request.method == 'POST':
        form = fifaModel(request.POST) 

        if form.is_valid():
            value = form.cleaned_data["VALUE_EUR"]
            release = form.cleaned_data["RELEASE_CLAUSE_EUR"] 
            age = form.cleaned_data["AGE"]
            potential = form.cleaned_data["POTENTIAL"]
            movement = form.cleaned_data["MOVEMENT_REACTION"]

            data = [[value,release , age, potential, movement]]

            fifamodel = joblib.load(MODEL_PATH)

            scaled = joblib.load(SCALER_PATH)
            transformed_data = scaled.transform(data)

            prediction = fifamodel.predict(transformed_data)[0]

            base_model_predictions = []
            for model in fifamodel.estimators_:
                   base_model_predictions.append(model.predict(transformed_data))

            variance_of_predictions = np.var(base_model_predictions)

            confidence_score = (1 - (98 / variance_of_predictions))*100

            # Create a new form with the 'PREDICTION' field set to the prediction
            prediction_form = fifaModel(initial={'PREDICTION': prediction, 'CONFIDENCE': confidence_score})
            # Clear other fields in the form
            prediction_form.fields['VALUE_EUR'].initial = None
            prediction_form.fields['RELEASE_CLAUSE_EUR'].initial = None
            prediction_form.fields['AGE'].initial = None
            prediction_form.fields['POTENTIAL'].initial = None
            prediction_form.fields['MOVEMENT_REACTION'].initial = None

            return render(request, template_name, {'form': prediction_form})

    else:
        form = fifaModel()

    return render(request, template_name, {'form': form})





     
    


   


    
