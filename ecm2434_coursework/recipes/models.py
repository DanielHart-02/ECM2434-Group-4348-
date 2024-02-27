from django.db import models
from django.contrib.auth.models import User 

class Ingredient_Ratings(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.CharField(max_length=255)
    rating = models.IntegerField()

class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipe_title = models.CharField(max_length=200)
    recipe_ingredients = models.CharField(max_length=200)
    preparation = models.CharField(max_length=200)
    prep_time = models.IntegerField(default=0)
    serves_num = models.IntegerField(default=1)
    def __str__(self):
        return self.recipe_title
