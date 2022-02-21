from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UpdateUser, UpdateProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUser( request.POST, instance = request.user)
        p_form = UpdateProfile( request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('profile')
    else:
        u_form = UpdateUser(instance = request.user)
        p_form = UpdateProfile(instance = request.user.profile)

    form = {'u_form': u_form, 'p_form':p_form }
    return render(request, 'users/profile.html', form)
