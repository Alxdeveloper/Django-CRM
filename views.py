from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sucessifully logged in')
        else:
            messages.error(request, 'Invalid user')
            return redirect('home')
    else:
        return render(request, 'home.html')
    return render(request, 'home.html')

def singout(request):
    logout(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')


def Register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
            return redirect('home')
        else:
            messages.success(request, 'Invalid data')
            return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})
            
    