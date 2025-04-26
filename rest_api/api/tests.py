from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from status.models import Status

class AccountTests(APITestCase):
    
    
    def setUp(self):
        new_user=User(username="test_user_1",password="12345678!")
        new_user.save()
        status=Status(text="sample text",user=new_user)
        status.save()
        status=Status(text="sample text",user=new_user)
        status.save()
        
    def test_create_account(self):
       
        url = reverse('status_view')
        response = self.client.get(url, format='json')
        status_list=response.data
        self.assertEqual(len(status_list),2)
        self.assertEqual(response.status_code,200)
       
        