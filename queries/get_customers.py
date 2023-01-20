from entities.customer import Customer


class GetCustomers:
    def __init__(self) -> None:
        self.customers = [
            Customer(
                first_name="Daniel",
                last_name="Leal",
                tax_id="91641705272",
                email="danielleal94@gmail.com",
                phone="91992727942",
            ),
            Customer(
                first_name="Yasmin",
                last_name="Leal",
                tax_id="00868506281",
                email="yasminn.p3@gmail.com",
                phone="991684986",
            ),
            Customer(
                first_name="Maria",
                last_name="Clara",
                tax_id="91641705272",
                email="danielleal94@gmail.com",
                phone="91992727942",
            ),
        ]
