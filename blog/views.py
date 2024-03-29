from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.template.defaultfilters import slugify


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:'blog.Post'.
    **Context**
    ''post''
        An instance of :model:'blog.Post'

    **Template**
    :template:'blog/post_detail.html'
    """
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    like_count = post.likes.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "'Your comment submitted as DRAFT for Approval! "
                "It will be available for public view once the"
                " Administrator approves it!'"
            )

            return HttpResponseRedirect(
                reverse('post_detail', args=[slug]))
    # Added this line as the Comments were duplicating when f5 was pressed
    comment_form = CommentForm()
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'commented': False,
            'like_count': like_count,
            'liked': liked,
            'comment_count': comment_count,
            'comment_form': comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments was originally part of post_detail.html
    To allow the user to see his likes and commented posts I moved
    the functionality to edit_comment.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(instance=comment)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "'Comment submitted as DRAFT for Approval! It"
                " will be available for public view once the"
                " Administrator approves it!'"
                )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(
                request,
                message.ERROR,
                'Error updating comment!'
                )

    else:
        return render(
            request,
            'blog/edit_comment.html',
            {
                'comment': comment,
                'comment_form': comment_form,
            },
        )


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
                request,
                messages.SUCCESS,
                'Comment deleted!'
                )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Add Like functionality to Post that user likes
class PostLike(View):

    def post(self, request, slug, *arg, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Add Like functionality to Post that user likes #
class PostCreate(View):
    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "'Post submitted as DRAFT for Approval! It will be available"
                " for public view once the Administrator approves it!'"
                )
            return HttpResponseRedirect(
                reverse(
                    'post_detail',
                    args=[post.slug])
            )

    def get(self, request, *args, **kwargs):
        post_form = PostForm()
        return render(
            request,
            'blog/post_create.html',
            {'post_form': post_form}
            )


def post_edit(request, slug, post_id):
    """
    View to edit posts
    """
    post = get_object_or_404(Post, slug=slug)
    post_form = PostForm(instance=post)

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            # Assuming 'post' is not supposed to be updated here, #
            # use a different field to assign the post object #
            post.author = request.user
            post.slug = slugify(post.title)
            post.status = "0"
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "'Post submitted as DRAFT for Approval! It will be available"
                " for public view once the Administrator approves it!'"
                )
            return HttpResponseRedirect(
                reverse('post_detail', args=[post.slug]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating post!'
            )

    return render(
        request,
        'blog/edit_post.html',
        {
            'post': post,
            'post_form': post_form,
        },
    )


def post_delete(request, slug, post_id):
    """
    view to delete post
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post = get_object_or_404(Post, pk=post_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own posts!'
            )

    return HttpResponseRedirect(reverse('profile'))
