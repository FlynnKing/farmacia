from classi import Persistenza
from classi.Persistenza import PersistenceFactory
import json


class Addresses:
    __address = 0  # PK
    __line_1_number_building = ""
    __line_1_number_street = ""
    __line_1_area_locality = ""
    __city = ""
    __zip_postcode = ""
    __state_province_county = ""
    __country = ""
    __other_address_details = ""

    def __init__(self, address, line_1_number_building, line_1_number_street, line_1_area_locality, city, zip_postcode, state_province_county, country, other_address_details):
        self.__id = id(self)
        self.__address = address
        self.__line_1_number_building = line_1_number_building
        self.__line_1_number_street = line_1_number_street
        self.__line_1_area_locality = line_1_area_locality
        self.__city = city
        self.__zip_postcode = zip_postcode
        self.__state_province_county = state_province_county
        self.__country = country
        self.__other_address_details = other_address_details

        # f"Customers('{self.address}', {self.line_1_number_building}, {self.line_1_number_street}, {self.line_1_area_locality}, {self.city}, {self.other_customer_details}, {self.zip_postcode}, {self.state_province_county}, {self.country}, {self.other_address_details})"
        # [{'nome': 'd', 'cognome': '', 'email': '', 'telefono': '', 'sito_web': ''}]
    def get_json(self):
        addr = {}
        for c in self.__dict__:
            addr[c] = self.__dict__[c]
        return addr

    def set_json(self):
        pass

    def get_address(self):  #
        return self.__address

    def set_address(self, address):  #
        self.__address = address
        return self.__address

    def get_line_1_number_building(self):
        return self.__line_1_number_building

    def set_line_1_number_building(self, line_1_number_building):
        self.__line_1_number_building = line_1_number_building

    def get_line_1_number_street(self):
        return self.__line_1_number_street

    def set_line_1_number_street(self, line_1_number_street):
        self.__line_1_number_street = line_1_number_street

    def get_line_1_area_locality(self):
        return self.__line_1_area_locality

    def set_line_1_area_locality(self, line_1_area_locality):
        self.__line_1_area_locality = line_1_area_locality

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_zip_postcode(self):
        return self.__zip_postcode

    def set_zip_postcode(self, zip_postcode):
        self.__zip_postcode = zip_postcode

    def get_state_province_county(self):
        return self.__state_province_county

    def set_state_province_county(self, state_province_county):
        self.__state_province_county = state_province_county

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_other_address_details(self):
        return self.__other_address_details

    def set_other_address_details(self, other_address_details):
        self.__other_address_details = other_address_details
