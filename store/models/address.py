from django.db import models

from . import Customer


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    cep = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.name}'s Address: {self.address}"
