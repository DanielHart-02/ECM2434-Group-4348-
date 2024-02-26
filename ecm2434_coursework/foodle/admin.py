from django.contrib import admin

from recipes.models import Recipes
from .models import MealEvents
from users.models import UserProfile

admin.site.register(Recipes)
admin.site.register(UserProfile)
admin.site.register(MealEvents)