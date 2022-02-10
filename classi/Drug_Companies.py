class Drug_Companies:
    id = 0  # PK
    company_name = ""
    other_company_details = ""
    def __init__(self, lastid, company_name, other_company_details):
        self.id = lastid + 1
        self.company_name = company_name
        self.other_company_details = other_company_details

    def get_id(self):
        return self.id  #

    def get_company_name(self):
        return self.company_name

    def set_company_name(self, company_name):
        self.company_name = company_name

    def get_other_company_details(self):
        return self.other_company_details

    def set_other_company_details(self, other_company_details):
        self.other_company_details = other_company_details
