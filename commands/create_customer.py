import re


class CreateCustomer:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        tax_id: str,
        email: str,
        phone: str,
    ):
        self.first_name = self._is_valid_name(first_name)
        self.last_name = self._is_valid_name(last_name)
        self.tax_id = self._is_valid_tax_id(tax_id)
        self.email = self._is_valid_email(email)
        self.phone = phone

    @staticmethod
    def _is_valid_name(name) -> str:
        if 3 > len(name) > 20:
            raise ValueError("Invalid name length")
        return name

    @staticmethod
    def _is_valid_tax_id(tax_id: str) -> str:
        if len(tax_id) != 11:
            raise ValueError("Invalid tax_id length")
        return tax_id

    @staticmethod
    def _is_valid_email(email: str) -> str:
        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )

        if not re.fullmatch(regex, email):
            raise ValueError("It's not an email address.")
        return email
