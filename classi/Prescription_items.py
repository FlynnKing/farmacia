class Prescription_items:
    __id = 0  # PF
    __drug_id = 0  # PF
    __prescription_quantity = ""
    __instructions_to_customer = ""

    def __init__(self, drug_id, prescription_quantity, instructions_to_customer):
        self.__id = id
        self.__drug_id = drug_id
        self.__prescription_quantity = prescription_quantity
        self.__instructions_to_customer = instructions_to_customer

    def get_json(self):
        Pre_items = {}
        for c in self.__dict__:
            Pre_items[c] = self.__dict__[c]
        return Pre_items

    def set_json(self):
        pass

    def get_id(self):
        return self.__id

    def get_drug_id(self):
        return self.__drug_id

    def set_drug_id(self, drug_id):
        self.__drug_id = drug_id

    def get_prescription_quantity(self):
        return self.__prescription_quantity

    def set_prescription_quantity(self, prescription_quantity):
        self.__prescription_quantity = prescription_quantity

    def get_instructions_to_customer(self):
        return self.__instructions_to_customer

    def set_instructions_to_customer(self, instructions_to_customer):
        self.__instructions_to_customer = instructions_to_customer
