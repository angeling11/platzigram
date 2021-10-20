from django.shortcuts import redirect
from django.urls import reverse

# Middleware catalog
class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user has their picture and biography.
    """
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response