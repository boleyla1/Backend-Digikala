from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm , UpdateUser


def Shop(request):
    Prudocts = Product.objects.all()
    return render(request, 'shop/index.html', {'Prudocts': Prudocts})


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "با موفقیت وارد شدید")
            return redirect('shop')
        else:
            messages.success(request, "مشکلی در لاگین وجود دارد!")
            return redirect('login')
    else:
        return render(request, 'shop/login.html')


def UserLogout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید')
    return redirect('shop')


def Rigester(request):
    context = {"errors":[]}
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # FirstName = form.cleaned_data.get('FirstName')
            # LastName = form.cleaned_data.get('LastName')
            # Email = form.cleaned_data.get('Email')
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.success(request,"پسورد یکسان نیست")
                return render(request,'shop/rigester.html')
            user = authenticate(username=username, password=password1,password2=password2)
            login(request, user)
            messages.success(request, "اکانت شما ساخته شد")
            return redirect('shop')
        else:
            messages.success(request, "مشکلی در ثبت نام شما وجود دارد")
            return redirect('register')
    else:
        return render(request, 'shop/rigester.html', {'form': form})


def product(request, pk):
    product1 = Product.objects.get(id=pk)
    return render(request, 'shop/product.html', {'product': product1})


def category(request, cat):
    cat = cat.replace('-', ' ')
    try:
        categorylist = Category.objects.get(Name=cat)
        products = Product.objects.filter(Category=categorylist)
        return render(request, 'shop/category.html', {'products': products, "category": categorylist})
    except:
        messages.success(request, "دسته بندی وچود ندارد")
        return redirect('shop')


def category_summary(request):
    allcat = Category.objects.all()

    return render(request, 'shop/category_summary.html', {'allcat': allcat})


def updateuser(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        userform = UpdateUser(request.POST or None,instance=current_user)
        if userform.is_valid():
            userform.save()
            login(request,current_user)
            messages.success(request,"پروفایل شما ویرایش شد")
            return redirect('shop')
        return render(request, 'shop/updateuser.html', {'userform': userform})
    else:
        messages.success(request,"ابتدا باید لاگین شوید")