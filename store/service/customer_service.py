import requests

from store.models import Customer
from store.models.address import Address, CustomerAddress


class CustomerService:

    def customer_list(self):
        return Customer.objects.all()

    def fetch_and_create_customers(self):
        api_url = 'https://jsonplaceholder.typicode.com/users'

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                users = response.json()
                for user in users:
                    existing_customer = Customer.objects.filter(
                        email=user['email']).first()

                    if existing_customer:
                        existing_customer.name = user['name']
                        existing_customer.save()
                    else:
                        customer = Customer(
                            name=user['name'],
                            email=user['email'],
                            phone=user['phone']
                        )
                        customer.save()

                    address_data = user.get('address', None)

                    if address_data:
                        address, created = Address.objects.get_or_create(
                            street=address_data['street'],
                            city=address_data['city'],
                            cep=address_data['zipcode']
                        )

                        if not existing_customer:
                            customer_address, created = CustomerAddress.objects.get_or_create(
                                customer=customer,
                                address=address
                            )

                return True
            else:
                print(f'Error in API request: {response.status_code}')
                return False
        except Exception as e:
            print(f'Error accessing the API: {str(e)}')
            return False
