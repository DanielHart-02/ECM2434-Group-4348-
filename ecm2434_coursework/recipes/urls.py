from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path("view/<int:recipe_id>", views.view_recipe, name="view_recipe"),
]