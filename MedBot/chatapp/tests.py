from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class chatappTest(TestCase):

    def test_chatapp(self):
        self.assertEqual(reverse('chatapp'), '/chatapp/chatapp/')  
        
    def test_chatapp_view(self):
        response = self.client.get(reverse('chatapp'))
        self.assertTemplateUsed(response, 'chatapp.html')
