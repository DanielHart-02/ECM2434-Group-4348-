from django import forms
from datetime import datetime
from recipes.models import Recipe
from .models import Group
from django.core.exceptions import ValidationError


def not_in_past(date_time):
    if datetime.now().date() >= date_time:
        raise ValidationError("Your event date cannot be in the past")


class CreateMealEvent(forms.Form):
    recipe_choices = []
    for recipe in Recipe.objects.all():
        recipe_choices.append((recipe.recipe_id, recipe.recipe_title))

    recipe = forms.ChoiceField(choices=recipe_choices)
    date_time = forms.DateField(validators=[not_in_past])


class createGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
