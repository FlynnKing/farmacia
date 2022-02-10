class Drug_Companies:
    __id = 0  # PK
    __company_name = ""
    __other_company_details = ""

    def __init__(self, company_name, other_company_details):
        self.__id = id(self)
        self.__company_name = company_name
        self.__other_company_details = other_company_details

    def get_json(self):
        Drug_Comp = {}
        for c in self.__dict__:
            Drug_Comp[c] = self.__dict__[c]
        return Drug_Comp

    def set_json(self):
        pass

    def get_id(self):
        return self.__id  #

    def get_company_name(self):
        return self.__company_name

    def set_company_name(self, company_name):
        self.__company_name = company_name

    def get_other_company_details(self):
        return self.__other_company_details

    def set_other_company_details(self, other_company_details):
        self.__other_company_details = other_company_details
