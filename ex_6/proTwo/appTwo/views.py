from django.shortcuts import render
#from appTwo.models import users
from appTwo.forms import NewUserForm
# Create your views here.
def my_users(request):

    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Occured!")

    return render(request, 'appTwo/users.html', {'form':form })

def index(request):
    my_dict = {'insert_string':'<a href="/users">users</a>'}
    return render(request,"appTwo/index.html", context=my_dict)
