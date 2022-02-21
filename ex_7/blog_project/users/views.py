from django.shortcuts import render,redirect
from users.forms import userForm, userUpdateForm, profileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_register(request):
    if request.method == 'POST':

        forms = userForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            forms.save()
            messages.success(request, f'Account created for { username }!')
            return redirect('blog-home')
    else:
        forms = userForm()

    return render(request, 'users/register.html', {'forms':forms})

@login_required
def profile(request):
    if request.method == 'POST':
        u_forms = userUpdateForm(request.POST, instance = request.user)
        p_forms = profileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_forms.is_valid() and p_forms.is_valid():
            u_forms.save()
            p_forms.save()
            #return redirect('blog-home')
    else:
        u_forms = userUpdateForm(instance = request.user)
        p_forms = profileUpdateForm(instance = request.user.profile)

    ctx ={'u_forms':u_forms, 'p_forms':p_forms}
    return render(request, 'users/profile.html', ctx)
