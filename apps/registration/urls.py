from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    # PasswordChangeView,
    # PasswordChangeDoneView,
    PasswordResetView,
)
from registration.apps import RegistrationConfig
from registration.views import (
    Signup,
    UserUpdateView,
    CustomPasswordChangeView
)


app_name = RegistrationConfig.name
urlpatterns = [
    path('s-inscrire.html', Signup.as_view(), name='signup'),
    path('se-connecter.html', LoginView.as_view(), name="login"),
    path('se-deconnecter.html', LogoutView.as_view(), name="logout"),
    path('mon-compte.html', UserUpdateView.as_view(), name="profile"),
    path('changer-mot-de-passe.html', CustomPasswordChangeView.as_view(), name='password_change'),
    # path('changer-mot-de-passe-confirmation.html', PasswordChangeDoneView.as_view(), name='password_change_done'),


    path('redefinir-mot-de-passe.html', PasswordResetView.as_view(
        # template_name='account/password_reset.html',
        # email_template_name='account/password_reset_email.html',
        # subject_template_name='account/password_reset_subject.txt'
    ), name='password_reset'),

]
