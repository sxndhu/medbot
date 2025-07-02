from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your tests here.
class accountstets(TestCase):
    def setUp(self):
        self.testangad = User.objects.create_user(username = 'angadtest', password = 'testpassword')

    def test_signup(self):
        self.assertEqual(reverse('signup'), '/accounts/signup/')

    def test_signup_form_valid(self):
        form = SignupForm(data = {
            'username' : 'emily',
            'first_name' :'Emily',
            'last_name' : 'Rose',
            'email' : 'emily@gmail.com',
            'password1' : 'nurse123',
            'password2' : 'nurse123'
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form = SignupForm(data = {
            'username' : 'emily',
            'first_name' :'Emily',
            'last_name' : 'Rose',
            'email' : 'emily@gmail.com',
            'password1' : 'emily123',
            'password2' : 'emily123'
        })

        self.assertFalse(form.is_valid())

    def test_login_url(self):
        self.assertEqual(reverse('login'), '/accounts/login/')

    def test_logout_url(self):
        self.assertEqual(reverse('logout'), '/accounts/logout/')

    def test_login_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'angadtest', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(response.url, reverse('home'))  

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200) 

    def test_logout_view(self):
        self.client.login(username='angadtest', password='testpassword')

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have successfully logged out")