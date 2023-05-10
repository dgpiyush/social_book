from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import SignUpForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the accounts index.")

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
        else:
            print(form.errors)
            return render(request, "accounts/register.html", {"form": form})
        
    return render(request, "accounts/register.html", {"form": SignUpForm()})
                  
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})
    
    
    return render(request, "accounts/login.html")


def logout_page(request):
    logout(request)
    return redirect('home')