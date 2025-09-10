from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import RegisterForm, LoginForm  
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# ----- Login -----
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.role == "seller":
                return redirect("seller_dashboard")
            else:
                return redirect("buyer_dashboard")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

# ----- Register -----
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  
            user.save()
            
            if user.role == "seller":
                group = Group.objects.get(name="Seller")
            else:
                group = Group.objects.get(name="Buyer")
            user.groups.add(group)
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Profile updated successfully!")
            except Exception as e:
                messages.error(request, f"Error saving profile: {e}")
                print(e)  
            return redirect("profile")
        else:
            print(form.errors)  
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "users/profile.html", {"form": form})

def buyer_dashboard(request):
    orders = request.user.buyer_orders.all().order_by('-created_at')
    return render(request, "users/buyer_dashboard.html", {"orders": orders})

