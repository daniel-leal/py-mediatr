from mediatr import Mediator

from commands.create_customer import CreateCustomer
from handlers.customer_handlers import (
    CreateCustomerHandler,
    GetCustomersHandler,
)
from queries.get_customers import GetCustomers

if __name__ == "__main__":
    mediator = Mediator()
    mediator.register_handler(CreateCustomerHandler)
    mediator.register_handler(GetCustomersHandler)

    # Command
    command = CreateCustomer(
        first_name="Daniel",
        last_name="Leal",
        tax_id="91641705272",
        email="danielleal94@gmail.com",
        phone="91992727942",
    )
    result = mediator.send(command)
    print(result.name)

    # query
    query = GetCustomers()
    result = mediator.send(query)
    print(result)
