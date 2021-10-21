# Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'author': {
            'name': 'Montse Cortes',
            'picture': 'https://source.unsplash.com/rDEOVtE7vOs/150x150'
        },
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'photo': 'https://source.unsplash.com/gG70fyu3qsg/600x900'
    },
    {
        'title': 'Beatiful',
        'author': {
            'name': 'Liz Nahal',
            'picture': 'https://source.unsplash.com/BGz8vO3pK8k/150x150'
        },
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'photo': 'https://source.unsplash.com/RfoISVdKM4U/600x900'
    },
    {
        'title': 'Eyes',
        'author': {
            'name': 'Joana Hash',
            'picture': 'https://source.unsplash.com/6_9TzlWhpdM/150x150'
        },
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'photo': 'https://source.unsplash.com/tCJ44OIqceU/600x900'
    },
    {
        'title': 'Innocence',
        'author': {
            'name': 'Julia Noa',
            'picture': 'https://source.unsplash.com/a4pyoiTdSqI/150x150'
        },
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
        'photo': 'https://source.unsplash.com/pJqfhKUpCh8/600x900'
    }
]

# Funtion that render the feed of the app
@login_required
def list_posts(request):
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
