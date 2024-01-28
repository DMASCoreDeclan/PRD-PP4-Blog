from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm # custom form that adds fields to the register.html form

# Add custom form: UserRegisterForm so it can be used here 

# Create your views here.
'''
inspired by Corey Schafer:
https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
This VIEW is for /register.
It checks to see if its a POST request and then applies validation.
if the validation is not correct, the view is returned to the user with the
information that does not need to be changed and removes the information that
does need to be changed.
Successful registration returns you to the home page with a message.SUCCESS displayed 
at the top of the screen
'''
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}, welcome to blog|star')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request, 
        'users/register.html',
        {
            'form': form
            }
            )