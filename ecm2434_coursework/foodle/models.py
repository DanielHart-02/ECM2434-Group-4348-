from django.db import models

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    number_members = models.IntegerField(default=0)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    foodle_score = models.IntegerField(default=0)
    food_score = models.IntegerField(default=0)
    group_id = models.ForeignKey(Group, null = True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.username


class Admin(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user_id

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipe_title = models.CharField(max_length=200)
    recipe_ingredients = models.CharField(max_length=200)
    preparation = models.CharField(max_length=200)
    prep_time = models.IntegerField(default=0)
    serves_num = models.IntegerField(default=1)
    def __str__(self):
        return self.recipe_title
