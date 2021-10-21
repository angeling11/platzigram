# Django
from django.forms import ModelForm
from posts.models import Post

# Create the form class.
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'profile', 'title', 'photo']
