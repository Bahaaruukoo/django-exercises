from django.shortcuts import render

# Create your views here.
def home(request):
    myDic = {
    'data':'This is my proTwo'
    }
    return render(request, 'appTwo/help.html', context=myDic)
