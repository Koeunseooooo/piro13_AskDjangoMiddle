from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect(profile)
    else:
        form=UserCreationForm()
    return render(request, 'accounts/signup.html'),{
        'form':form,
    }


@login_required
def profile(request):
    request.user
    return render(request, 'accounts/profile.html')
