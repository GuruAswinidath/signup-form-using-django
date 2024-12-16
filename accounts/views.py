from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            return render(request, 'accounts/landing.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


def landing(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/landing.html', {'user': request.user})
    else:
        return redirect('login')  # Redirect to login page if user is not authenticated

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to the login page
