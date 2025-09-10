from django.urls import path
from .views import register_view, login_view
from django.contrib.auth.views import LogoutView
from orders.views import seller_dashboard
from . import views

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", views.profile_update, name="profile"),
    path('seller/dashboard/', seller_dashboard, name='seller_dashboard'),
]

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login') 
