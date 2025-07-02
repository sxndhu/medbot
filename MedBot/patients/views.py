from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientAddForm, PatientUpdateForm

def viewpatientdata(request):
    patient = Patient.objects.all()
    return render(request, 'viewpatientdata.html', {'patient' : patient })


def addpatient(request):
    if request.method == 'POST':
        form = PatientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewpatientdata')
    else:
        form = PatientAddForm()

    return render(request, 'addpatient.html', {'form' : form})

def updatepatientdata(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance = patient)

        if form.is_valid():
            form.save()
            return redirect('viewpatientdata')
       
    else:
        form = PatientUpdateForm(instance = patient)

    return render (request, 'updatepatientdata.html', {'form' : form, 'patient' : patient })

def deletepatientdata(request, id):
    patient = get_object_or_404(Patient, id = id)

    if request.method == 'POST':
        patient.delete()
        return redirect('viewpatientdata')


