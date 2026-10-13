from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("signup/", views.SignUpView.as_view(),
        name="signup"),

    path("login/", views.CustomLoginView.as_view(), name= "login"),

    path("profile/",login_required(views.ProfileView.as_view()), name="profile")

]