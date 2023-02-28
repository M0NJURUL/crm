from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders, 'customers':customers, 
               'total_orders':total_orders, 'orders_delivered':orders_delivered,
               'orders_pending':orders_pending}
    return render(request, 'accounts/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()


    context={'customer':customer, 'orders':orders, 'total_orders': total_orders}
    return render(request, 'accounts/customer.html', context)
