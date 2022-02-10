from classi import Customers, Physicians, Ref_Payment_Methods, Ref_Prescription_Status


class Prescriptions:
    customer = None
    physician = None
    payment_method_code = None
    prescription_status_code = None
    id = 0  # FK
    prescription_issued_date = ""  # *
    prescription_filled_date = ""
    other_details = ""

    def __init__(self, lastid, prescription_issued_date, prescription_filled_date, other_details):
        self.customer = Customers.Customers
        self.physician = Physicians.Physicians
        self.payment_method_code = Ref_Payment_Methods.Ref_Payment_Methods
        self.prescription_status_code = Ref_Prescription_Status.Ref_Prescription_Status
        self.id = lastid + 1
        self.prescription_issued_date = prescription_issued_date
        self.prescription_filled_date = prescription_filled_date
        self.other_details = other_details

    def get_customer(self):
        return self.customer_id

    def set_customer(self, customer):
        self.customer = customer
        return self.customer

    def get_physician_id(self):
        return self.physician_id

    def set_physician_id(self, physician):
        self.physician = physician
        return self.physician

    def get_payment_method_code(self):
        return self.payment_method_code

    def set_payment_method_code(self, payment_method_code):
        self.payment_method_code = payment_method_code
        return self.payment_method_code

    def get_prescription_status_code(self):
        return self.prescription_status_code

    def set_prescription_status_code(self, prescription_status_code):
        self.prescription_status_code = prescription_status_code

    def get_prescription_id(self):
        return self.prescription_id

    def set_prescription_id(self, prescription_id):
        self.prescription_id = prescription_id

    def get_prescription_issued_date(self):
        return self.prescription_issued_date

    def set_prescription_issued_date(self, prescription_issued_date):
        self.prescription_issued_date = prescription_issued_date

    def get_prescription_filled_date(self):
        return self.prescription_filled_date

    def set_prescription_filled_date(self, prescription_filled_date):
        self.prescription_filled_date = prescription_filled_date

    def get_other_details(self):
        return self.other_details

    def set_other_details(self, other_details):
        self.other_details = other_details

    def get___dict__(self):
        return self.__dict__

    def set___dict__(self, __dict__):
        self.__dict__ = __dict__

    def get___weakref__(self):
        return self.__weakref__

    def set___weakref__(self, __weakref__):
        self.__weakref__ = __weakref__

    def get___doc__(self):
        return self.__doc__

    def set___doc__(self, __doc__):
        self.__doc__ = __doc__
