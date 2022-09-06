from django.test import TestCase
from django.contrib.auth.models import User

from users.models import Profile

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='elliotanderson', password='password')

    def test_github(self):
        user = User.objects.get(username='elliotanderson')
        user.profile.github = "github.com/elliotanderson"
        self.assertEqual(user.profile.github, "github.com/elliotanderson")

    def test_job_title(self):
        user = User.objects.get(username='elliotanderson')
        user.profile.job_title = "Chaos Engineer"
        self.assertEqual(user.profile.job_title, "Chaos Engineer")
