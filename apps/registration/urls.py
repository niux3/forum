from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from registration.apps import RegistrationConfig
from registration.views import Signup


app_name = RegistrationConfig.name
urlpatterns = [
    path('s-inscrire.html', Signup.as_view(), name='signup'),
    path('se-connecter.html', LoginView.as_view(), name="login"),
    path('se-deconnecter.html', LogoutView.as_view(), name="logout"),
]
