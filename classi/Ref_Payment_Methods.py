class Ref_Payment_Methods:
    payment_method_code = ""  # PK
    payment_method_description = ""

    # eg Cash, Credit Card
    def __init__(self, payment_method_code, payment_method_description):
        self.payment_method_code = payment_method_code
        self.payment_method_description = payment_method_description

    def get_json(self):
        Ref_Pay_Met = {}
        for c in self.__dict__:
            Ref_Pay_Met[c] = self.__dict__[c]
        return Ref_Pay_Met

    def set_json(self):
        pass

    def get_payment_method_code(self):
        return self.payment_method_code

    def set_payment_method_code(self, payment_method_code):  # non so se ha senso metterlo
        self.payment_method_code = payment_method_code

    def get_payment_method_description(self):
        return self.payment_method_description

    def set_payment_method_description(self, payment_method_description):
        self.payment_method_description = payment_method_description
