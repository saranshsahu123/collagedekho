# users/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # Redirect to the login page after successful signup
    success_url = reverse_lazy('login')
    # Specify the template to use for the signup form
    template_name = 'registration/signup.html'