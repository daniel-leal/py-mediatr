from entities.customer import Customer


class GetCustomers:
    def __init__(self) -> None:
        self.customers = Customer.get_all()
