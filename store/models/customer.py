from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
