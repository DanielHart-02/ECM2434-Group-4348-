from django.db import models
from django.contrib.auth.models import User 

class IngredientRating(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField()

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipe_title = models.CharField(max_length=200)
    recipe_ingredients = models.CharField(max_length=200)
    preparation = models.TextField()
    prep_time = models.PositiveIntegerField(default=0)
    serves_num = models.PositiveIntegerField(default=1)
    co2_per_portion = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.recipe_title