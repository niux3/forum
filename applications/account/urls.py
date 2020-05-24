from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"
urlpatterns = [
    path('s-inscrire', views.signup, name="signup"),
    path('se-deconnecter', auth_views.LogoutView.as_view(), name="logout"),
    path('se-connecter', auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path('redefinir-mot-de-passe', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html',
        email_template_name='account/password_reset_email.html',
        subject_template_name='account/password_reset_subject.txt'
    ), name='password_reset'),
    path('redefinition-mot-de-passe', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html',
    ), name="password_reset_done"),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path("redefinition-mot-de-passe-complete", auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
    name='password_reset_complete'),
    path('changer-mot-de-passe', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
    name='password_change'),
    path('changer-mot-de-passe-confirmation', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
    name='password_change_done'),
]