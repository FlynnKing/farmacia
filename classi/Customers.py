from classi import Adresses
import json


class Customers:
    id = 0  # PK
    address = None
    customer_name = ""
    date_became_customer = ""
    credit_card_number = ""
    card_expiry_date = ""
    other_customer_details = ""

    def __init__(self,lastid, customer_name, date_became_customer, credit_card_number, card_expiry_date,other_customer_details, address):
        self.id = lastid + 1
        self.customer_name =customer_name
        self.date_became_customer = date_became_customer
        self.credit_card_number = credit_card_number
        self.card_expiry_date = card_expiry_date
        self.other_customer_details = other_customer_details
        self.address = address

    def __repr__(self) -> str:
        return f"Customers('{self.id}', {self.customer_name}, {self.date_became_customer}, {self.credit_card_number}, {self.card_expiry_date}, {self.other_customer_details}, {self.address})"

    def get_id(self):
        return self.id

    def get_address(self, address):  # id di Address
        return print(address)

    def set_address(self, address):  # id di Address
        self.address = address

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_date_became_customer(self):
        return self.date_became_customer

    def set_date_became_customer(self, date_became_customer):
        self.date_became_customer = date_became_customer

    def get_credit_card_number(self):
        return self.credit_card_number

    def set_credit_card_number(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def get_card_expiry_date(self):
        return self.card_expiry_date

    def set_card_expiry_date(self, card_expiry_date):
        self.card_expiry_date = card_expiry_date

    def get_other_customer_details(self):
        return self.other_customer_details

    def set_other_customer_details(self, other_customer_details):
        self.other_customer_details = other_customer_details
