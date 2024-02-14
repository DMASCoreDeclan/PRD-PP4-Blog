from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


'''
This model allows a user to upload a profile picture to their profile
inspired by Corey Schafer:
https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.user.username}s Profile" 