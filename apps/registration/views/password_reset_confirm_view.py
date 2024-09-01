from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('registration:password_reset_complete')
