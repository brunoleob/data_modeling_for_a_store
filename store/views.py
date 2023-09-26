from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CustomerRegistrationForm
from .models import Customer
from .serializers import CustomerSerializer
from .service.customer_service import CustomerService


def index(request):
    print(request.user)
    return render(request, 'store.html')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_success.html')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register.html', {'form': form})


class CustomerDetailView(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        if not customer:
            return redirect('index')

        serializer = CustomerSerializer(customer)
        return render(request, 'customer_detail.html', {'customer': serializer.data})
