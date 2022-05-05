# Django
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/img/instagram.png', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    re_path(r'^favicon\.ico$', favicon_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
