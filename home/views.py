from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from users.models import CustomUser
from users.forms import CustomLoginForm

def index(request):
    return render(request, 'home/index.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def login_view(request):
    form = CustomLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = request.POST.get('role')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.role == role:
                login(request, user)
                if role == 'technician':
                    messages.success(request, "Succesfuly logged in. " + user.username)
                    return redirect('technician_dashboard')
                else:
                    messages.success(request, "Succesfuly logged in. " + user.username )
                    return redirect('client_dashboard')
            else:
                messages.error(request, "Invalid credentials or role mismatch.")

    return render(request, 'home/login.html', {'form': form})
