from django import forms
from .models import Patient

genders = [('Male' , 'Male'), ('Female' , 'Female'), ('Other' , 'Other')]

class PatientAddForm(forms.ModelForm):
    gender = forms.ChoiceField(choices = genders)
    email = forms.EmailField(max_length = 200)
    
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone_number', 'email' ]
        widgets = { 'date_of_birth': forms.DateInput(attrs={'type': 'date'})}

class PatientUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices = genders)
    email = forms.EmailField(max_length = 200)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone_number', 'email' ]
        widgets = { 'date_of_birth': forms.DateInput(attrs={'type': 'date'})}