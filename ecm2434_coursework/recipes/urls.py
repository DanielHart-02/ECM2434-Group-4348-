from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path("create", views.create_recipe, name="create_recipe"),
    path("recipe_details/<int:recipe_id>", views.recipe_details, name="recipe_details"),
    path("all_recipies", views.all_recipies, name="all_recipies"),
]
