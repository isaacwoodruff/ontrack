from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from users.models import Profile

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='elliotalderson', password='password')

    def test_github(self):
        user = User.objects.get(username='elliotalderson')
        user.profile.github = "github.com/elliotalderson"
        self.assertEqual(user.profile.github, "github.com/elliotalderson")

    def test_job_title(self):
        user = User.objects.get(username='elliotalderson')
        user.profile.job_title = "Chaos Engineer"
        self.assertEqual(user.profile.job_title, "Chaos Engineer")

class AuthenticationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='elliotalderson')
        user.set_password('password')
        user.save()

    def test_login_view(self):
        response = self.client.post('/', {'username':'elliotalderson', 'password':'password'}, follow=True)
        self.assertTrue(response.context['user'].is_active)
