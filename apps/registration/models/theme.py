from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=32, default='default')

    def __str__(self):
        return self.name
