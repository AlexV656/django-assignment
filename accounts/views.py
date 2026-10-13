from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



class CustomLoginView(LoginView):
   # success_url = reverse_lazy('profile')
    # next_page = reverse_lazy('home')
    template_name = "registration/login.html"



class ProfileView(TemplateView):
    template_name = "profile.html"