# Django
from django.forms import ModelForm
from posts.models import Post


class PostForm(ModelForm):
    """Create the form class."""
    class Meta:
        model = Post
        fields = ['user', 'profile', 'title', 'photo']
