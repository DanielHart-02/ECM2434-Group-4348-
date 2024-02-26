from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def join_group(request, group_name):
    try:
        to_join = Group.objects.get(name = group_name)
    except Group.DoesNotExist:
        return HttpResponse("The group you are trying to join does not exist")
    
    if (request.GET.get('leave_group_btn')):
        for g in request.user.groups.all():
            g.user_set.remove(request.user)
    
    if (request.user.groups.count() == 0):
        to_join.user_set.add(request.user)
        return redirect('foodle:home')
    else:
        return render(request,'users/leave_group.html')