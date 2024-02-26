from django.contrib import admin

from .models import Recipe
from users.models import UserProfile

admin.site.register(Recipe)
admin.site.register(UserProfile)