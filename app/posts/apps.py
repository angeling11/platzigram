# Django
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post config."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Posts'
