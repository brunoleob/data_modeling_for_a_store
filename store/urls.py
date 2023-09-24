from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer-list/", views.customer_list, name="customers-list")

]
