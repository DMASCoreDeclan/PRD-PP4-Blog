from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


'''
This model allows a user to upload a profile picture to their profile
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.user.username}s Profile" 