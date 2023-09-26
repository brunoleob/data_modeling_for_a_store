from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=15, default='No phone')
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    cep = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.name}'s Address: {self.address}"
