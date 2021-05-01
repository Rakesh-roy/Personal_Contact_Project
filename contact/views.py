from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Personal_Contact_Project import settings
from contact.models import ContactModel, LoggedInUser
from contact.forms import ContactForm, UserRegistrationForm
import requests
import json

from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def contactHome(request):
    # url = requests.get('http://127.0.0.1:8000/api.contacts/')
    # data = json.loads(url.text)
    data = ContactModel.objects.filter(owner=request.user).order_by('name')
    return render(request, 'index.html', {'contacts': data})
    # try:
    #     user = LoggedInUser.objects.get(user_id=request.user.id)
    #     if user.session_key:
    #         data = ContactModel.objects.filter(owner=request.user).order_by('name')
    #         return render(request,'index.html',{'contacts':data})
    # except:
    #     return HttpResponse("you are not allowed to access this page..!!")


@login_required(login_url='login')
def addContact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Saved Successfully')
        else:
            messages.error(request, form.errors)
        return redirect('add_contact')
    return render(request,'add_contact.html',{'form':form})


@login_required(login_url='login')
def viewContact(request):
    contact = ContactModel.objects.get(id=request.GET.get('contact'))
    return render(request,'view_contact.html',{'contact':contact})


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        rememberme = request.POST.get('rememberme')
        if rememberme is not None:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user=user)
            return redirect('home')

        # if uname == 'admin' and pwd == 'admin':
        #     return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')


def registerUser(request):
    form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Account Successfully Created")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, 'register.html',{"form":form})


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def removeContact(request):
    ContactModel.objects.get(id=request.GET.get('contact')).delete()
    return redirect('home')
