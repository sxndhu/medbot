from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SymptomsForm
from .predictor import predictDisease

# Create your views here.

def checksymptom(request):
    if request.method == 'POST':
        form = SymptomsForm(request.POST)
        if form.is_valid():
            symptom1 = form.cleaned_data["symptom1"]
            symptom2 = form.cleaned_data["symptom2"]
            symptom3 = form.cleaned_data["symptom3"]
            symptom4 = form.cleaned_data["symptom4"]
            symptom5 = form.cleaned_data["symptom5"]
            symptom6 = form.cleaned_data["symptom6"]

            input_string = f"{symptom1}, {symptom2}, {symptom3}, {symptom4}, {symptom5}, {symptom6}"
            pred = predictDisease(input_string)
            final_prediction = pred['final_prediction']
            accuracy = pred['final_score']
            return render(request, 'checksymptom.html', {'form' : form, 'prediction_is' : final_prediction, 'accuracy' : accuracy})
            
        else:
            return render(request, 'checksymptom.html', {'form' : form})
    else:
        return render(request, 'checksymptom.html', {'form' : SymptomsForm()})
