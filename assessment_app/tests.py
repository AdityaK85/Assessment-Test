from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserDetails

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = reverse('user_registration')
        self.valid_payload = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpassword',
            'referral_code': ''
        }
    
    def test_user_registration_success(self):
        response = self.client.post(self.registration_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserDetails.objects.count(), 1)
        self.assertIn('api_token', response.data)
    
    def test_user_registration_existing_email(self):
        UserDetails.objects.create(name='Existing User', email='test@example.com', password='existingpassword')
        response = self.client.post(self.registration_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['response'], 'Email Already Exists')

class GetUsersInfoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.info_url = reverse('get_users_info')

    def test_get_users_info(self):
        UserDetails.objects.create(name='User 1', email='user1@example.com', password='password1')
        UserDetails.objects.create(name='User 2', email='user2@example.com', password='password2')
        response = self.client.get(self.info_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['payload']), 2)


class GetReferralUsersInfoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.referral_info_url = reverse('get_referral_users_info')

    def test_get_referral_users_info(self):
        UserDetails.objects.create(name='Referral User 1', email='referral1@example.com', password='password1', referral_code='REF001')
        UserDetails.objects.create(name='Referral User 2', email='referral2@example.com', password='password2', referral_code='REF002')
        response = self.client.get(self.referral_info_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['payload']), 2)