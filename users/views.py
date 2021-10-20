from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')

# User logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
