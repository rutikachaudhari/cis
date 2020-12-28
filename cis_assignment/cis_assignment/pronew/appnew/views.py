from django.shortcuts import render
from django.shortcuts import redirect

from appnew.forms import UserForm,UserProfileInfoForm,ProductForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from appnew.models import *

# Create your views here.
def index(request):
    return render(request,'appnew/index.html')


@login_required
def special(request):
    return HttpResponse("you are logged in")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'appnew/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("your account was inactive")
        else:
            print("Someone tried to login and failed")
            print("they used username:{} and password:{}".format(username,password))
            return HttpResponse("invalid login details given")
    else:
        return render(request,'appnew/login.html', {})


def emp(request):

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            if form.errors:

                print(form.errors)
            return HttpResponseRedirect('/show/')

    else:
        form = ProductForm(request.POST)
    return render(request,'appnew/prodcrud.html',{'form':form})



def show(request):
    product = Product.objects.all()
    return render(request,'appnew/productdata.html',{'product':product})

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request,'appnew/edit.html', {'product':product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/show/")
    return render(request, 'appnew/edit.html', {'product': product})

def destroy(request, id):
    product = Product.objects.get(id=id)
    roduct.delete()
    return redirect('/show/')
