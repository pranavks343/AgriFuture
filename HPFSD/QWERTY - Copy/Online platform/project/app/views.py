from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def base(request):
    return render(request, 'app/Base.html')

# Home View
'''def Home(request):
    return render(request, 'app/buynow.html')'''

# Registration View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'app/register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'app/register.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'app/register.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Optional: Log the user in after registration
        login(request, user)

        messages.success(request, "Registration successful! You can log in now.")
        return redirect('login')

    return render(request, 'app/register.html')


def cart(request):
    return render(request, 'app/cart.html')

def buy_now(request):
    return render(request, 'app/buy_now.html')

def product_list(request):
    # Logic to fetch products from the database
    return render(request, 'app/products.html')

def product_detail(request, product_id):
    # Logic to fetch the specific product by product_id from the database
    return render(request, 'app/product_detail.html')


# Login View
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('products')  # Redirect to the profile page or any other page
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'app/login.html')


# Logout View
def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# Profile View (Login Required)

def profile(request):
    return render(request, 'app/profile.html')

def seeds(request):
    return render(request, 'app/products/seeds.html')

def login_first(request):
    return render(request, 'app/Disclaimer/login_first.html')

def smart_equipments(request):
    return render(request, 'app/products/smart_equipments.html')

def about(request):
    return render(request, 'app/about.html')


# Products View
def products(request):
    return render(request, 'app/products.html')


def equipments(request):
    return render(request, 'app/products/equipments.html')


def buy_now(request):
    return render(request, 'app/buy_now.html')