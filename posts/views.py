# Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# Funtion that render the feed of the app
@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', { 'posts': posts})

# Create new post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )
