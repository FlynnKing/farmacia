from classi import Drug_Companies


class Drugs_and_Medication:
    company_id = None
    id = 0  # PK
    drug_name = ""
    drug_cost = ""
    drug_available_date = ""  # *
    drug_withdrawn_date = ""
    drug_description = ""
    generic_yn = ""
    generic_equivalent_drug_id = ""
    other_drug_details = ""

    def __init__(self, lastid, drug_name, drug_cost, drug_available_date, drug_withdrawn_date, drug_description,
                 generic_yn, generic_equivalent_drug_id, other_drug_details):
        self.id = lastid + 1
        self.company_id = Drug_Companies.Drug_Companies
        self.drug_name = drug_name
        self.drug_cost = drug_cost
        self.drug_available_date = drug_available_date
        self.drug_withdrawn_date = drug_withdrawn_date
        self.drug_description = drug_description
        self.generic_yn = generic_yn
        self.generic_equivalent_drug_id = generic_equivalent_drug_id
        self.other_drug_details = other_drug_details

    def get_company_id(self):
        return self.company_id

    def set_company_id(self, company_id):
        self.company_id = company_id

    def get_id(self):
        return self.id  #

    def get_drug_name(self):
        return self.drug_name

    def set_drug_name(self, drug_name):
        self.drug_name = drug_name

    def get_drug_cost(self):
        return self.drug_cost

    def set_drug_cost(self, drug_cost):
        self.drug_cost = drug_cost

    def get_drug_available_date(self):
        return self.drug_available_date

    def set_drug_available_date(self, drug_available_date):
        self.drug_available_date = drug_available_date

    def get_drug_withdrawn_date(self):
        return self.drug_withdrawn_date

    def set_drug_withdrawn_date(self, drug_withdrawn_date):
        self.drug_withdrawn_date = drug_withdrawn_date

    def get_drug_description(self):
        return self.drug_description

    def set_drug_description(self, drug_description):
        self.drug_description = drug_description

    def get_generic_yn(self):
        return self.generic_yn

    def set_generic_yn(self, generic_yn):
        self.generic_yn = generic_yn

    def get_generic_equivalent_drug_id(self):
        return self.generic_equivalent_drug_id

    def set_generic_equivalent_drug_id(self, generic_equivalent_drug_id):
        self.generic_equivalent_drug_id = generic_equivalent_drug_id

    def get_other_drug_details(self):
        return self.other_drug_details

    def set_other_drug_details(self, other_drug_details):
        self.other_drug_details = other_drug_details

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
