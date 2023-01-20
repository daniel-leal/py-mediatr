from commands.create_customer import CreateCustomer
from entities.customer import Customer
from queries.get_customers import GetCustomers


class CreateCustomerHandler:
    def handle(self, request: CreateCustomer):
        customer = Customer(
            request.first_name,
            request.last_name,
            request.tax_id,
            request.email,
            request.phone,
        )

        return customer


class GetCustomersHandler:
    def handle(self, request: GetCustomers):
        customers = request.customers
        names = []
        for c in customers:
            names.append(c.name)
        return ", ".join(names)
