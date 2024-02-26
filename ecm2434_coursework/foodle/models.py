from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator
from recipes.models import Recipes
    
class Foodle(models.Model):
    date = models.AutoField(primary_key=True)
    daily_word = models.CharField(max_length=5)
    score = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(200)])

class MealEvents(models.Model):
    Meal_Event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)