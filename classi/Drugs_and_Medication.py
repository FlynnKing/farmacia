from classi import Drug_Companies


class Drugs_and_Medication:
    company_id = None
    __id = 0  # PK
    __drug_name = ""
    __drug_cost = ""
    __drug_available_date = ""  # *
    __drug_withdrawn_date = ""
    __drug_description = ""
    __generic_yn = ""
    __generic_equivalent_drug_id = ""
    __other_drug_details = ""

    def __init__(self, company_id, drug_name, drug_cost, drug_available_date, drug_withdrawn_date, drug_description,
                 generic_yn, generic_equivalent_drug_id, other_drug_details):
        self.__id = id(self)
        self.__company_id = company_id
        self.__drug_name = drug_name
        self.__drug_cost = drug_cost
        self.__drug_available_date = drug_available_date
        self.__drug_withdrawn_date = drug_withdrawn_date
        self.__drug_description = drug_description
        self.__generic_yn = generic_yn
        self.__generic_equivalent_drug_id = generic_equivalent_drug_id
        self.__other_drug_details = other_drug_details

    def get_json(self):
        Dru_and_Medi = {}
        company_id_diz = {}
        for c in self.__dict__:
            Dru_and_Medi[c] = self.__dict__[c]
        for c in self.__company_id.__dict__:
            company_id_diz[c] = self.__company_id.__dict__[c]
        Dru_and_Medi['company_id'] = company_id_diz
        return Dru_and_Medi

    def set_json(self):
        pass

    def get_company_id(self):
        return self.__company_id

    def set_company_id(self, company_id):
        self.__company_id = company_id

    def get_id(self):
        return self.__id  #

    def get_drug_name(self):
        return self.__drug_name

    def set_drug_name(self, drug_name):
        self.__drug_name = drug_name

    def get_drug_cost(self):
        return self.__drug_cost

    def set_drug_cost(self, drug_cost):
        self.__drug_cost = drug_cost

    def get_drug_available_date(self):
        return self.__drug_available_date

    def set_drug_available_date(self, drug_available_date):
        self.__drug_available_date = drug_available_date

    def get_drug_withdrawn_date(self):
        return self.__drug_withdrawn_date

    def set_drug_withdrawn_date(self, drug_withdrawn_date):
        self.__drug_withdrawn_date = drug_withdrawn_date

    def get_drug_description(self):
        return self.__drug_description

    def set_drug_description(self, drug_description):
        self.__drug_description = drug_description

    def get_generic_yn(self):
        return self.__generic_yn

    def set_generic_yn(self, generic_yn):
        self.__generic_yn = generic_yn

    def get_generic_equivalent_drug_id(self):
        return self.__generic_equivalent_drug_id

    def set_generic_equivalent_drug_id(self, generic_equivalent_drug_id):
        self.__generic_equivalent_drug_id = generic_equivalent_drug_id

    def get_other_drug_details(self):
        return self.__other_drug_details

    def set_other_drug_details(self, other_drug_details):
        self.__other_drug_details = other_drug_details