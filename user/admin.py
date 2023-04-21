from django.contrib import admin
from .models import CustomUser, Verification

admin.site.register(CustomUser)
admin.site.register(Verification)