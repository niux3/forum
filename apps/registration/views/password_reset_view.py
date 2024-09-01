from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('registration:password_reset_done')
