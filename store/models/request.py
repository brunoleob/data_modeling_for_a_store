# from django.db import models

# from .customer import \
#     Customer  # Importe o modelo Customer para estabelecer a relação


# class Request(models.Model):
#     request_id = models.AutoField(primary_key=True)
#     datetime = models.DateTimeField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Request {self.request_id} by {self.customer.name}"
