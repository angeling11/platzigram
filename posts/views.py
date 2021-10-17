from django.shortcuts import render
from django.http import HttpResponse

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

# Create your views here.
def list_posts(request):
    return render(request, 'feed.html', { 'posts': posts})
