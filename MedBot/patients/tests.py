from django.test import TestCase, Client
from .models import Patient
from .views import viewpatientdata, addpatient, updatepatientdata, deletepatientdata
from django.urls import reverse
from .forms import PatientAddForm, PatientUpdateForm

# Create your tests here.
class PatientTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_viewpatientdata(self):
        patient = Patient.objects.create(first_name='Angad', 
        last_name='Singh', 
        date_of_birth='1999-07-27',
        gender='Male',
        address='21, Noda',
        phone_number='987654321',
        email='angadsingh@gmail.com')

        response = self.client.get(reverse('viewpatientdata'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewpatientdata.html')
        self.assertEqual(len(response.context['patient']), 1)
        self.assertEqual(response.context['patient'][0].first_name, 'Angad')


    def test_addpatient_url(self):
        self.assertEqual(reverse('addpatient'), '/patients/addpatient/')

    def test_addpatient_view(self):
        new_patient = {
        'first_name' : 'Angad', 
        'last_name' : 'Singh', 
        'date_of_birth' : '1999-07-27',
        'gender' : 'Male',
        'address' : '21, Noda',
        'phone_number' : '987654321',
        'email' : 'angadsingh@gmail.com'
        }
        
        response = self.client.post(reverse('addpatient'),new_patient)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.count(), 1)


    def test_updatepatientdata_url(self):
        patient = Patient.objects.create(first_name='Angad', 
        last_name='Singh', 
        date_of_birth='1999-07-27',
        gender='Male',
        address='21, Noda',
        phone_number='987654321',
        email='angadsingh@gmail.com')
        self.assertEqual(reverse('updatepatientdata', args=[patient.id]) , f'/patients/updatepatientdata/{patient.id}')

    def test_updatepatientdata_view(self):
        patient = Patient.objects.create(first_name='Angad', 
        last_name='Singh', 
        date_of_birth='1999-07-27',
        gender='Male',
        address='21, Noda',
        phone_number='987654321',
        email='angadsingh@gmail.com')

        updated_data = {
        'first_name' : 'Angad', 
        'last_name' : 'Singh', 
        'date_of_birth' : '1999-07-27',
        'gender' : 'Male',
        'address' : '21, Noda',
        'phone_number' : '8527348980',
        'email' : 'angadsingh@gmail.com'
        }

        response = self.client.post(reverse('updatepatientdata', args=[patient.id]), updated_data)
        self.assertEqual(response.status_code, 302)
        updated_patient = Patient.objects.get(id=patient.id)
        self.assertEqual(updated_patient.phone_number, '8527348980')


    def test_deletepatientdata(self):
        patient = Patient.objects.create(first_name='Angad', 
        last_name='Singh', 
        date_of_birth='1999-07-27',
        gender='Male',
        address='21, Noda',
        phone_number='987654321',
        email='angadsingh@gmail.com')


        response = self.client.post(reverse('deletepatientdata', args=[patient.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.count(), 0)
        self.assertEqual(response.url, reverse('viewpatientdata'))
