from django import forms
from datetime import datetime
from recipes.models import Recipe
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone

def not_in_past(date_time):
    if timezone.now() >= date_time:
        raise ValidationError("Your event date cannot be in the past")


class CreateMealEvent(forms.Form):
    recipe_choices = []
    for recipe in Recipe.objects.all():
        recipe_choices.append((recipe.recipe_id, recipe.recipe_title))

    recipe = forms.ChoiceField(choices=recipe_choices)
    date_time = forms.DateTimeField(validators=[not_in_past], widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'})
)


class createGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
