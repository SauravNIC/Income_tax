from django.contrib import admin
from home.models import Feedback

# Register your models here.
admin.site.register(Feedback)


def __str__(self):
    return self.name