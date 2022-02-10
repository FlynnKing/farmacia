from classi import Customers, Physicians, Ref_Payment_Methods, Ref_Prescription_Status


class Prescriptions:
    __customer = None
    __physician = None
    __payment_method_code = None
    __prescription_status_code = None
    __id = 0  # FK
    __prescription_issued_date = ""  # *
    __prescription_filled_date = ""
    __other_details = ""

    def __init__(self, customer, physician, payment_method_code, prescription_status_code, prescription_issued_date,
                 prescription_filled_date, other_details):
        self.__customer = customer  # oggetto
        self.__physician = physician  # oggetto
        self.__payment_method_code = payment_method_code  # oggetto
        self.__prescription_status_code = prescription_status_code  # oggetto
        self.__id = id(self)
        self.__prescription_issued_date = prescription_issued_date
        self.__prescription_filled_date = prescription_filled_date
        self.__other_details = other_details

    def get_json(self):
        Pres = {}
        cust = {}
        phy = {}
        payment_method = {}
        prescription_status = {}
        for c in self.__dict__:
            Pres[c] = self.__dict__[c]
        for c in self.customer.__dict__:
            cust[c] = self.customer.__dict__[c]
        for c in self.physician.__dict__:
            phy[c] = self.physician.__dict__[c]
        for c in self.payment_method_code.__dict__:
            payment_method[c] = self.payment_method_code.__dict__[c]
        for c in self.prescription_status_code.__dict__:
            prescription_status[c] = self.prescription_status_code.__dict__[c]
        Pres['customer'] = cust
        Pres['physician'] = phy
        Pres['payment_method_code'] = payment_method
        Pres['prescription_status_code'] = prescription_status
        return Pres

    def set_json(self):
        pass

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
