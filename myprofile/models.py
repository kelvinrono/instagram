from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = models.ImageField(upload_to = 'gallery/', null=True, blank=True, default='download.jpeg')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)
