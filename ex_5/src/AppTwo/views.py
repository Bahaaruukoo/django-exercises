from django.shortcuts import render
from django.http import HttpResponse
from model import Model
# Create your views here.

def index(request):
    myDic = {'insert_me':"Hello I am from views.py! "}
    return render(request, 'first_app/index.html', context=myDic)

def help(request):
    cont= {
    'one':'this is help page from views'
    }
    return render(request,"first_app/help.html", context=cont)

def get_users(request):
    user_object = Users.object.all()
    user_dics = {
        'user_ing':'user_object'
    }
    return render(request, "first_app/index.html", context=user_dics)
