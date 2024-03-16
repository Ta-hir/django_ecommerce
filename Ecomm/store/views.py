from django.shortcuts import render,redirect
from .models import Product, Category,Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAdress

from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

# Create your views here.

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # querry database products model
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        # test for null
        if not searched:
            messages.success(request, 'sorry that product does not exixst')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched':searched})
    else:
        return  render(request, 'search.html', {})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, 'User has been updated')
            return redirect('home')
        return render(request, 'update_user.html', {"user_form":user_form})
    else:
        messages.success(request, 'you must be logged in to access that page')
        return redirect('home')

def update_profile(request):
    if request.user.is_authenticated:
        # get current user
        current_user = Profile.objects.get(user__id=request.user.id)
         # get current user shipping info
        shipping_user = ShippingAdress.objects.get(user__id=request.user.id)
        # get original form
        form = UserInfoForm(request.POST or None, instance=current_user)
        # get user shipping form
        shipping_form =  ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            # save original form
            form.save()
            # save shipping form
            shipping_form.save()
            messages.success(request, 'Your info has has been updated')
            return redirect('home')
        return render(request, 'update_profile.html', {'form':form, 'shipping_form':shipping_form})
    else:
        messages.success(request, 'you must be logged in to access that page')
        return redirect('home')

    return render(request, 'update_profile.html', {})


def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)    
        context = {"category":category, "products":products}
        return render(request, 'category.html', context)
    except:
        messages.success(request,('this category does not exist'))
        return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'product.html', context)


def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            # do some shopping cart magic
            current_user = Profile.objects.get(user__id=request.user.id)
            # get their saved cart from the database
            saved_cart = current_user.old_cart
            # convert database string to  python dictionary
            if saved_cart:
                converted_carte = json.loads(saved_cart)
                # add loadedcart dictionary to session
                cart = Cart(request)
                # loop throughthe cart and add items from the dictionary
                for key,value in converted_carte.items():
                    cart.db_add(product=key, quantity=value)



            messages.success(request,('login successful'))
            return redirect('home')
        else:
            messages.success(request,('therewas an error while logging in, please check your credentials'))
            return redirect('login')
        
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('you have been loggedout,thanks for stopping by..'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('User name created please fill out your usser info below.'))
            return redirect('update_profile')
        else:
            messages.success(request,('problem while registering, please try agin'))
            return redirect('register')
    else:
        return render(request, 'register.html', context)
    

def category_summary(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_summary.html', context)

def update_user(request):

    return render(request, 'update_user.html', {})