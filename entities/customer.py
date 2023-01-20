class Customer:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        tax_id: str,
        email: str,
        phone: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.tax_id = tax_id
        self.email = email
        self.phone = phone

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def formatted_tax_id(self):
        return "{}.{}.{}-{}".format(
            self.tax_id[:3],
            self.tax_id[3:6],
            self.tax_id[6:9],
            self.tax_id[9:],
        )
