import json
from classi.Adresses import Addresses


class Customers:
    __id = 0  # PK
    __address = None
    __customer_name = ""
    __date_became_customer = ""
    __credit_card_number = ""
    __card_expiry_date = ""
    __other_customer_details = ""

    def __init__(self, customer_name, date_became_customer, credit_card_number, card_expiry_date, other_customer_details, address):
        self.__id = id(self)
        self.__customer_name = customer_name
        self.__date_became_customer = date_became_customer
        self.__credit_card_number = credit_card_number
        self.__card_expiry_date = card_expiry_date
        self.__other_customer_details = other_customer_details
        self.__address = address

    def modifica(self, key, value):
        if key.lower() == "address":
            self.set_address(value)
        if key.lower() == "customer_name":
            self.set_customer_name(value)
        if key.lower() == "date_became_customer":
            self.set_date_became_customer(value)
        if key.lower() == "credit_card_number":
            self.set_credit_card_number(value)
        if key.lower() == "card_expiry_date":
            self.set_card_expiry_date(value)
        if key.lower() == "other_customer_details":
            self.set_other_customer_details(value)
        else:
            print ("modifica non riuscita")

        
    def get_json(self):
        cust = {}
        addr = {}
        for c in self.__dict__:
            cust[c] = self.__dict__[c]
        for c in self.__address.__dict__:
            addr[c] = self.__address.__dict__[c]
        cust['_Customers__address'] = addr
        return cust

    def set_json(self, jsonstr):
        d = json.loads(jsonstr)
        if '_Customers__address' in d.keys():
            addr = Addresses()
            self.__address =  addr.set_from_dict(d['_Customers__address'])

        #fp = open("tutto.dat", 'r')
        #x = fp.read()
        #fp.close()
        #leggi = json.loads(x)
        #return leggi

    def get_id(self):
        return self.__id

    def get_address(self):  # id di Address
        return self.__address

    def set_address(self, address):  # id di Address
        self.__address = address

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def get_date_became_customer(self):
        return self.__date_became_customer

    def set_date_became_customer(self, date_became_customer):
        self.__date_became_customer = date_became_customer

    def get_credit_card_number(self):
        return self.__credit_card_number

    def set_credit_card_number(self, credit_card_number):
        self.__credit_card_number = credit_card_number

    def get_card_expiry_date(self):
        return self.__card_expiry_date

    def set_card_expiry_date(self, card_expiry_date):
        self.__card_expiry_date = card_expiry_date

    def get_other_customer_details(self):
        return self.__other_customer_details

    def set_other_customer_details(self, other_customer_details):
        self.__other_customer_details = other_customer_details
