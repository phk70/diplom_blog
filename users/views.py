from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    if request.method == "POST":
        contact_number = request.POST.get("contact_number")
        city = request.POST.get("city")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image, city=city, sex=sex, age=age)
        profile.save()
        return redirect('users:profile', permanent=True)
    return render(request, "users/profile.html")


def user_profile(request, id):
    user = User.objects.get(id=id)
    return render(request, "users/user_profile.html", {"user":user})