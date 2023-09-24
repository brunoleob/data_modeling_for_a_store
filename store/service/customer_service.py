from store.models import Customer


class CustomerService:
    def customer_list(self):
        return Customer.objects.all()
