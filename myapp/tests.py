from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Application

class UserProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.create(user=self.user, phone_number='1234567890', address='Taddress')
        self.assertEqual(user_profile.__str__(), 'testuser')

class ApplicationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.application = Application.objects.create(
            user=self.user,
            title='Test Application',
            description='Test Description'
        )

    def test_application_creation(self):
        self.assertEqual(self.application.__str__(), 'Test Application - testuser')

    def test_application_defaults(self):
        self.assertEqual(self.application.status, 'new')
