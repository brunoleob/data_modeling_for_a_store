from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from .forms import CustomerRegistrationForm
from .service.customer_service import CustomerService


def index(request):
    print(request.user)
    return render(request, 'store.html')


def customer_list(request):
    customer_service = CustomerService()
    customers = customer_service.customer_list()
    return render(request, 'customer_list.html', {'customers': customers})


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_success.html')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register.html', {'form': form})


# def register_success(request):
#     return render(request, 'register_success.html')


# def register_failed(request):
#     return render(request='register_failed.html')
