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
        tax_id="36974125846",
        email="daniel@email.com",
        phone="91992727481",
    )
    # Handler
    mediator.send(command)

    # Command
    command = CreateCustomer(
        first_name="Yasmin",
        last_name="Leal",
        tax_id="15975324862",
        email="yasmin@email.com",
        phone="91992727481",
    )

    # Handler
    mediator.send(command)

    # Command
    command = CreateCustomer(
        first_name="André",
        last_name="Leal",
        tax_id="84812135482",
        email="andre@email.com",
        phone="91992727481",
    )

    # Handler
    mediator.send(command)

    # query
    query = GetCustomers()

    # Handler
    result = mediator.send(query)
    print(result)
