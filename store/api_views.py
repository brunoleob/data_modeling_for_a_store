from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Customer
from store.serializers import CustomerSerializer
from store.service.customer_service import CustomerService


class CustomerListAPIView(APIView):
    def get(self, request):
        customer_service = CustomerService()
        customers = customer_service.customer_list()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
