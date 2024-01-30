'''
Inspired by: 
https://youtu.be/FdVuKt_iuSI?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1608

Django docs: 
https://docs.djangoproject.com/en/5.0/topics/signals/

Django’s built-in signals let user code get notified of certain actions.
This is used to add a default profile picture stored on Cloudinary when
the user SAVES or UPDATES their registration form
'''

from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender
from django.dispatch import receiver # receiver
from .models import Profile # the model use by the function


@receiver(post_save, sender=User) 
# call this function when the User is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
# call this function when the User is changed or updated
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

