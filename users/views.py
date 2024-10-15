from django.shortcuts import render, redirect

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()            
            login(request, user)
            return redirect('blog:post_list', permanent=True)
    form = NewUserForm()        
    return render(request, 'users/register.html', {"form": form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
