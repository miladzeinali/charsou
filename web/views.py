from django.shortcuts import render,redirect
from Product.models import *
from django.contrib import messages
from cart.models import Order,OrderItem
from account.models import Favorits,Userprofile
from django.contrib.auth.models import User
from account.models import Address

def Home(request):
    sales = Product.objects.filter(Sale=True)
    news = Product.objects.all()
    orderitems = []
    countitems = []
    total = 0
    countFave = 0
    countitems = len(orderitems)
    user = request.user
    if user.is_authenticated:
        try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            try:
                order = Order.objects.get(user=user,status='Wpay')
                orderitems = OrderItem.objects.filter(order=order)
            except:
                pass
            countitems = len(orderitems)
            for item in orderitems:
                total += item.quantity*item.price
        except:
            pass
    return render(request,'home.html',{'sales':sales,'news':news,'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})

def Shop(request):
    products = Product.objects.all()[0:4]
    return render(request,'products.html',{products:'products'})

def Dashbord(request):
    orderitems = []
    countitems = []
    total = 0
    orderitems = []
    countFave = 0
    favorits = []
    countitems = len(orderitems)
    countFave = len(favorits)
    user = request.user
    if user.is_authenticated:
        # try:
            favorits = Favorits.objects.filter(user=user)
            countFave = len(favorits)
            try:
                order = Order.objects.get(user=user,status='Wpay')
                orderitems = OrderItem.objects.filter(order=order)
            except:
                pass
            countitems = len(orderitems)
            for item in orderitems:
                total += item.quantity*item.price
        # except:
        #     pass
            return render(request,'cart.html',{'orderitems':orderitems,'countfave':countFave,'countitems':countitems,
                                       'total':total})
    else:
        return redirect('account:register')

def about(request):
   return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
