from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    # PasswordChangeView,
    # PasswordChangeDoneView,
    # PasswordResetView,
    PasswordResetDoneView,
    # PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from registration.apps import RegistrationConfig
from registration.views import (
    Signup,
    UserUpdateView,
    CustomPasswordChangeView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    UserDetail,
)


app_name = RegistrationConfig.name
urlpatterns = [
    path('s-inscrire.html', Signup.as_view(), name='signup'),
    path('se-connecter.html', LoginView.as_view(), name="login"),
    path('se-deconnecter.html', LogoutView.as_view(), name="logout"),
    path('mon-compte.html', UserUpdateView.as_view(), name="profile"),
    path('detail-<str:username>-<int:id>.html', UserDetail.as_view(), name="user_detail"),
    path('changer-mot-de-passe.html', CustomPasswordChangeView.as_view(), name='password_change'),

    # this view doesn't exists because redirection after change password (registration:password_change)
    # path('changer-mot-de-passe-confirmation.html', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('mot-de-passe-oublie.html', CustomPasswordResetView.as_view(), name='password_reset'),
    path('redefinition-mot-de-passe.html', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('redefinition-mot-de-passe/<str:uidb64>/<str:token>.html', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("mot-de-passe-modifie.html", PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
