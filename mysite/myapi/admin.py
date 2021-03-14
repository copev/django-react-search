from django.contrib import admin

# Register your models here.
from .models import Organization, Profile

admin.site.register(Organization)
admin.site.register(Profile)