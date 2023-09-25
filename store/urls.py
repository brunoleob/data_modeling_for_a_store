from django.urls import path

from store.api_views import CustomerListAPIView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer-list/", views.customer_list, name="customers-list"),
    path("register/", views.register_customer, name="register"),

]
