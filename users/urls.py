# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # Django's built-in login view
    # It will look for 'registration/login.html' by default
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    # Django's built-in logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]