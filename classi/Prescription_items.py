class Prescription_items:
    id = 0  # PF
    drug_id = 0  # PF
    prescription_quantity = ""
    instructions_to_customer = ""

    def __init__(self, lastid, prescription_quantity, instructions_to_customer):
        self.id = lastid + 1
        self.prescription_quantity = prescription_quantity
        self.instructions_to_customer = instructions_to_customer

    def get_id(self):
        return self.id

    def get_drug_id(self):
        return self.drug_id

    def set_drug_id(self, drug_id):
        self.drug_id = drug_id

    def get_prescription_quantity(self):
        return self.prescription_quantity

    def set_prescription_quantity(self, prescription_quantity):
        self.prescription_quantity = prescription_quantity

    def get_instructions_to_customer(self):
        return self.instructions_to_customer

    def set_instructions_to_customer(self, instructions_to_customer):
        self.instructions_to_customer = instructions_to_customer
