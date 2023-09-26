from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_customer, name="register"),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer-detail')

]
