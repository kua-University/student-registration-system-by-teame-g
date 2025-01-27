from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


#home view
def home(request):
    return render(request, 'users/home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create-checkout-session')  # Redirect to a homepage after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

#aboutus view
def aboutus(request):
    return render(request, 'users/aboutus.html')

def payment_success(request):
    return render(request, 'users/success.html')