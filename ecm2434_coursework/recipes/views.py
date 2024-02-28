from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Recipe, IngredientRating
from .forms import RecipeForm


@login_required
<<<<<<< HEAD
def all_recipies(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/all_recipies.html", {"recipes": recipes})


@login_required
def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_details.html", {"recipe": recipe})

=======
def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "foodle/recipe_details.html", {"recipe": recipe})


@login_required
def view_all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "foodle/all_recipies.html", {"recipes": recipes})
>>>>>>> 7944c4204305c9cd31dc74539d9a59c5c3f3a490

def create_recipe(request):
    ingredient_ratings = IngredientRating.objects.all()
    form = RecipeForm(request.POST or None)
    context = {"form": form, "ingredient_ratings": ingredient_ratings}
    if request.method == "POST":
        if form.is_valid():
            ingredients = form.cleaned_data.get("ingredients")
            quantities = [
                int(quantity) for quantity in form.cleaned_data.get("quantities")
            ]
            serves = form.cleaned_data.get("serves_num")
<<<<<<< HEAD
            co2_score = get_score(ingredients, quantities, serves)

            formatted_ingredients = ""
=======
            sulphates_score = get_score(ingredients, quantities, serves)
            
            formatted_ingredients = ''
>>>>>>> 7944c4204305c9cd31dc74539d9a59c5c3f3a490

            for i in range(len(ingredients)):
                formatted_ingredients += (
                    ingredients[i] + " - " + str(quantities[i]) + "g"
                )
                if i < len(ingredients) - 1:
                    formatted_ingredients += ", "

            new_recipe = Recipe(
                user=request.user,
<<<<<<< HEAD
                recipe_title=form.cleaned_data.get("recipe_title"),
                recipe_ingredients=formatted_ingredients,
                preparation=form.cleaned_data.get("preparation"),
                prep_time=form.cleaned_data.get("prep_time"),
                serves_num=serves,
                co2_per_portion=co2_score,
=======
                recipe_title = form.cleaned_data.get("recipe_title"),
                recipe_ingredients = formatted_ingredients,
                preparation = form.cleaned_data.get("preparation"),
                prep_time = form.cleaned_data.get("prep_time"),
                serves_num = serves,
                sulphates_per_portion = sulphates_score
>>>>>>> 7944c4204305c9cd31dc74539d9a59c5c3f3a490
            )
            new_recipe.save()
            return redirect("recipes:view_all_recipes")
        return render(request, "recipes/create_recipe.html", context)
    else:
        return render(request, "recipes/create_recipe.html", context)


def get_score(ingredients, quantities, serves):
    score = 0
    for i in range(len(ingredients)):
        try:
            ingredient_rating = IngredientRating.objects.get(ingredient=ingredients[i])
            score += ingredient_rating.rating / 1000 * quantities[i] / serves
        except IngredientRating.DoesNotExist:
            continue
    return score
