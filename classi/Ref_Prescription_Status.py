import random
class Ref_Prescription_Status:
    prescription_status_code = ""  # PK
    prescription_status_description = ""

    # eg Filled, Part-Filled
    # eg Filled but not collected
    def __init__(self, payment_method_code, payment_method_description):
        self.payment_method_code = str(random.randint(10000000, 99999999))
        self.payment_method_description = payment_method_description

    def get_prescription_status_code(self):
        return self.prescription_status_code

    def set_prescription_status_code(self, prescription_status_code):
        self.prescription_status_code = prescription_status_code

    def get_prescription_status_description(self):
        return self.prescription_status_description

    def set_prescription_status_description(self, prescription_status_description):
        self.prescription_status_description = prescription_status_description
