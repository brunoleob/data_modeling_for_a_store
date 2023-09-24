from django.http import HttpResponse
from django.shortcuts import render

from .service.customer_service import CustomerService


def index(request):
    print(request.user)
    return HttpResponse("Hello, world. You're at the store index.")


def customer_list(request):
    customer_service = CustomerService()
    customers = customer_service.customer_list()
    return render(request, 'customer_list.html', {'customers': customers})
