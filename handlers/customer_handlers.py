from commands.create_customer import CreateCustomer
from entities.customer import Customer
from queries.get_customers import GetCustomers


class CreateCustomerHandler:
    def handle(self, request: CreateCustomer):
        customer = Customer(
            first_name=request.first_name,
            last_name=request.last_name,
            tax_id=request.tax_id,
            email=request.email,
            phone=request.phone,
        )

        customer.save()

        return customer


class GetCustomersHandler:
    def handle(self, request: GetCustomers):
        customers = request.customers
        names = []
        for c in customers:
            names.append(c.name)
        return ", ".join(names)
