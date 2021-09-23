from django.shortcuts import render, HttpResponse, redirect
from home.models import Feedback
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def about(request):
    return HttpResponse('About')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        feedback = Feedback(name=name,email=email,msg=msg)
        feedback.save()
        messages.success(request,'Thank You for the Feedback')

    return render(request,'feedback.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else :
            return render(request,'index.html')
    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')