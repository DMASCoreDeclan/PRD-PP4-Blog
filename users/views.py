from django.shortcuts import render, redirect
from django.contrib import messages

# ensures the profile view does not load unless you're logged in
from django.contrib.auth.decorators import login_required 

'''
Add custom form: UserRegisterForm form for register.html
Add custom form: UserUpdateForm form for register/profile.html
Add custom form: ProfileUpdateForm form for register/profile.html
'''
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Comment, Post
 

# Create your views here.

def register(request):
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}, welcome to blog|star, please log in')
            return redirect('account_login')
    else:
        form = UserRegisterForm()

    return render(
        request, 
        'users/register.html',
        {
            'form': form
            }
            )


'''
The profile page is available only after:
REGISTER - > LOGIN
If the User is not authenticated, the @login_required presents login.html,
and appends "?next=/register/profile/" to the end of the login url so that
after successful login, the user is redirected to their profile
'''
@login_required     
def profile(request):
    '''
    gathers the form fields of User/ProfileUpdateForm(s)
    and presents them in the return context for viewing within 
    users/profile.html prepopulated with the known details
    currently stored in admin/auth/user/<user_id>/ and
    admin/users/profile/<user_id>/
    '''
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST, 
            instance=request.user
            )  
        p_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'{request.user.username}, your account was successfully updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)  
        p_form = ProfileUpdateForm(instance=request.user.profile)
        user_comments = Comment.objects.filter(author=request.user)
        #Locate Liked posts of the logged in user
        user_liked_post = Post.objects.filter(likes__in=[request.user]) 
    

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_comments': user_comments,
        #display Liked posts of the logged in user
        'user_liked_post': user_liked_post,
    }

    return render(request, 'users/profile.html', context)


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('register/profile/profile.html', args=[slug]))