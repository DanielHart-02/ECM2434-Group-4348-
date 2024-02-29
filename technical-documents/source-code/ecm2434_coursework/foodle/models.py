from django.db import models
from django.contrib.auth.models import User, Group
from recipes.models import Recipe
    
class Foodle(models.Model):
    date = models.AutoField(primary_key=True)
    daily_word = models.CharField(max_length=5)
    score = models.PositiveBigIntegerField()

class MealEvent(models.Model):
    Meal_Event_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    score = models.PositiveBigIntegerField(default = 0)