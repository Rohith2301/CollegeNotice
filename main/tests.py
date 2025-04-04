from django.test import TestCase
from django.urls import reverse

class HomeURLTest(TestCase):
    def test_login_url_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class SignupURLTest(TestCase):
    def test_SignUp_url_exists(self):
        response = self.client.get(reverse('student_login'))
        self.assertEqual(response.status_code, 200)

class AboutURLTest(TestCase):
    def test_about_url_exists(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)