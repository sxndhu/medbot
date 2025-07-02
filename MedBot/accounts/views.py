from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, f"Account created successfully. Welcome, {user.username}!")
            return redirect('home')  # Redirect to a successful signup page
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"Logged in successfully. Welcome, {username}!")
                return redirect('home') 
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        messages.success(request, f"You have successfully logged out, {request.user.username}!")
        auth.logout(request)
        return render (request, 'home.html')
    return render (request, 'home.html')