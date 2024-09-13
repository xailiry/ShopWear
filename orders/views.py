from django.shortcuts import render


# Create your views here.


def order_detail(request):
    return render(request, 'orders/order.html')


def order_create(request):
    return render(request, 'orders/order-create.html')


def orders_list(request):
    return render(request, 'orders/orders.html')


def success(request):
    return render(request, 'orders/success.html')
