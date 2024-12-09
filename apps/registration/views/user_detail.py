from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from registration.models import Profile


class UserDetail(DetailView):
    template_name = 'registration/user_detail.html'

    def get_object(self):
        return get_object_or_404(
            Profile, 
            pk = self.kwargs.get('id')
        )
