from django.db import models
from django.contrib.auth.models import User

# This constant feeds into the values for choices in this line of 
# code # below: status = models.IntegerField(choices=STATUS, default=0)
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    # choices=STATUS in the following line facilitates the use of 
    # 0 or 1 to denote Draft or Published.  these Choices are 
    # defined in the constant variable STATUS, above
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)