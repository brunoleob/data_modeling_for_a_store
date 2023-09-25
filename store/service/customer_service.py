import requests

from store.models import Customer


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

                return True
            else:
                print(f'Error in API request: {response.status_code}')
                return False

        except Exception as e:
            print(f'Error accessing the API: {str(e)}')
            return False
