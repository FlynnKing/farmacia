import random


class Ref_Payment_Methods:
    payment_method_code = ""  # PK
    payment_method_description = ""

    # eg Cash, Credit Card
    def __init__(self, payment_method_code, payment_method_description):
        self.payment_method_code = str(random.randint(10000000, 99999999))
        self.payment_method_description = payment_method_description

    def get_payment_method_code(self):
        return self.payment_method_code

    def set_payment_method_code(self, payment_method_code): # non so se ha senso metterlo
        self.payment_method_code = payment_method_code

    def get_payment_method_description(self):
        return self.payment_method_description

    def set_payment_method_description(self, payment_method_description):
        self.payment_method_description = payment_method_description
