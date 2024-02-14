'''
Influenced by Corey Schafer:
https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6

forms.py is being created so that I can add custom fields to my register.html
These fields will be used as a basis for a profile page for registered users
'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # imported so we can change the PROFILE_PICTURE


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    # This telss the form which model it will interact with ie User
    class Meta:
        model = User
        # These are the fields presented on the form for filling them out
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
            ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # first_name is no longer mandatory #
        self.fields['first_name'].required = False
        # last_name is no longer mandatory #
        self.fields['last_name'].required = False


'''
Influenced by Corey Schafer:
https://youtu.be/CQ90L5jfldw?si=rK2dtPfLQfk8cP5e&t=105
These fields were/could have been populated upon registration
using register.html.  This form is on profile.html
so that users can CHANGE their Email, FirtName and LastName once logged in.
'''


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    # This telss the form which model it will interact with ie User
    class Meta:
        model = User
        # fields for changing {{ user.username }}, {{ user.email }},
        # {{ user.first_name }} and {{ user.last_name }} in profile.html
        fields = ['username', 'email', 'first_name', 'last_name']


'''
These fields were/could have been populated upon registration
using register.html.  This form is on profile.html
so that users can CHANGE their Email, FirtName and LastName once logged in.
'''


class ProfileUpdateForm(forms.ModelForm):

    # This tells the form which model it will interact with ie User
    class Meta:
        model = Profile
        # field for changing {{ user.profile.profile_picture.url }}
        # in profile.html
        fields = ['profile_picture']
