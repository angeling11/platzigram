# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.
    Ensure every user has their picture and biography."""
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update'), reverse('users:logout')]:
                    return redirect('users:update')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
