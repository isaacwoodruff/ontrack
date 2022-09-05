from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''
    The Profile model extends the user model with a one-to-one relationship.
    If the Profile is deleted then it automatically deletes the user too
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    github = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='img')

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
