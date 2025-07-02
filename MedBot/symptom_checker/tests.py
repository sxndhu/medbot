from django.test import TestCase
from django.urls import reverse
from .forms import SymptomsForm

# Create your tests here.

class symptomcheckerTest(TestCase):

    def test_symptomchecker(self):
        self.assertEqual(reverse('checksymptom'), '/symptom_checker/checksymptom/')  



class formTest(TestCase):
    def test_form_valid(self):
        test_symptoms = {
            'symptom1': 'itching',
            'symptom2': 'skin_rash',
            'symptom3': 'nodal_skin_eruptions',
        }
        form = SymptomsForm(data=test_symptoms)
        self.assertTrue(form.is_valid())

    def test_form_required_field(self):
        test_symptoms = {
            'symptom1': 'itching',
            'symptom2': 'skin_rash',
            # 'symptom3' required
        }
        form = SymptomsForm(data=test_symptoms)
        self.assertFalse(form.is_valid())

    def test_form_optional_fields(self):
        test_symptoms = {
            'symptom1': 'itching',
            'symptom2': 'skin_rash',
            'symptom3': 'nodal_skin_eruptions',
            'symptom4': 'headache',
            'symptom5': '',
        }
        form = SymptomsForm(data=test_symptoms)
        self.assertTrue(form.is_valid())

    def test_form_invalid_choice(self):
        test_symptoms = {
            'symptom1': 'itching',  
            'symptom2': 'skin_rashing',   # incorrect option chosen
            'symptom3': 'nodal_skin_eruptions',
        }
        form = SymptomsForm(data=test_symptoms)
        self.assertFalse(form.is_valid())