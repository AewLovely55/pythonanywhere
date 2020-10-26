from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login

# Create your views here.
def login(request):
    return render(request,'myweb/login.html')

def index(request):
    return render(request,'myweb/index.html')

def mulan(request):
    return render(request,'myweb/mulan.html')

def tenet(request):
    return render(request,'myweb/tenet.html')

def pmak(request):
    return render(request,'myweb/pmak.html')

def jom(request):
    return render(request,'myweb/jom.html')

def bad(request):
    return render(request,'myweb/bad.html')

def onward(request):
    return render(request,'myweb/onward.html')

def alive(request):
    return render(request,'myweb/alive.html')

def bwa(request):
    return render(request,'myweb/bwa.html')

def extr(request):
    return render(request,'myweb/extr.html')

def eng(request):
    return render(request,'myweb/eng.html')

def th(request):
    return render(request,'myweb/th.html')

def ka(request):
    return render(request,'myweb/ka.html')

def ct(request):
    return render(request,'myweb/ct.html')

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')