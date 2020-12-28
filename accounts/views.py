from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/register.html',{"form":form})

def loginPage(request):
    return render(request, 'accounts/login.html')

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    #total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    return render(request, 'accounts/dashboard.html', {"orders":orders, "customers":customers, "total_orders": total_orders, "delivered":delivered, "pending":pending})

def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {"products": products})

def customer(request, pk_test):
    customers=Customer.objects.get(id=pk_test)
    orders=customers.order_set.all()
    order_count=orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    return render(request, 'accounts/customer.html', {"customers":customers,"orders":orders, "order_count":order_count, "myFilter":myFilter})
#CRUD
def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/order_form.html', {"form":form})

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/order_form.html', {"form":form})


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html',{"order":order})

