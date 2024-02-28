from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import UserProfile
from .models import MealEvent
from recipes.models import Recipe
from .forms import CreateMealEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def user_in_group(user):
    return (user.is_authenticated and user.groups.count() == 1)


#TODO divert to join group page
def welcome(request):
    return render(request, "foodle/welcome.html")


@login_required
def home(request):
    return render(request, "foodle/home.html")


@login_required
def play(request):
    if request.method == "POST":
        request.user.userprofile.foodle_score += int(request.POST['score'])
        request.user.userprofile.save()
        return redirect('foodle:home')
    else:
        return render(request, 'foodle/foodle.html')


@user_passes_test(user_in_group, login_url='foodle:no_group')
def events(request):
    user_group = request.user.groups.first()
    cooking_events = MealEvent.objects.filter(group=user_group).order_by('-date_time')
    context = {"cooking_events": cooking_events}
    return render(request, "foodle/events.html", context)


@user_passes_test(user_in_group, login_url='foodle:no_group')
def create_event(request):
    if request.method == "POST":
        form = CreateMealEvent(request.POST)
        if form.is_valid():
            event_recipe = Recipe.objects.get(recipe_id=form.cleaned_data.get("recipe"))
            event_group = request.user.groups.first()
            event_score = max(0, (10 - event_recipe.co2_per_portion/10) * User.objects.filter(groups=event_group).count())
            new_event = MealEvent(
                user=request.user,
                group= event_group,
                date_time=form.cleaned_data.get("date_time"),
                recipe= event_recipe,
                score=event_score
            )
            new_event.save()
            return redirect('foodle:events')
            
    else:
        form = CreateMealEvent()
    return render(request, "foodle/create_event.html", {"form": form})

@login_required
def leaderboard(request):
    profiles = list(UserProfile.objects.all())
    profiles.sort(reverse=True, key=lambda profile: profile.foodle_score + profile.env_score)
    context = {"top_100_profiles": profiles[:100]}
    return render(request, "foodle/leaderboard.html", context)

def no_group(request):
    return HttpResponse("You must be part of a group to access this page")