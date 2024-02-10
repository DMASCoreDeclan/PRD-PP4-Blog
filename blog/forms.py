from .models import Comment, Category, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'friendly_name', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'featured_image', 'content', 'excerpt')