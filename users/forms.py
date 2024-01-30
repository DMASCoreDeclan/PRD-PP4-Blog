'''
Influenced by Corey Schafer: 
https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6

forms.py is being created so that I can add custom fields to my register.html
These fields will be used as a basis for a profile page for registered users
'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    # This telss the form which model it will interact with ie User
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] # These are the fields presented on the form for filling them out

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False # first_name is no longer mandatory
        self.fields['last_name'].required = False # last_name is no longer mandatory
        # self.fields['first_name'].initial = 'first_name'
        # self.fields['last_name'].initial = 'last_name'