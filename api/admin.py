from django.contrib import admin
from .models import (Profile, Poll, Choice, Vote)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
