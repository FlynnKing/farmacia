from classi import Persistenza
from classi.Persistenza import PersistenceFactory
import json

class Addresses:
    address = 0  # PK
    line_1_number_building = ""
    line_1_number_street = ""
    line_1_area_locality = ""
    city = ""
    zip_postcode = ""
    state_province_county = ""
    country = ""
    other_address_details = ""

    def __init__(self, address, line_1_number_building, line_1_number_street, line_1_area_locality, city, zip_postcode, state_province_county, country, other_address_details):
        self.id = self.last_id() + 1
        self.address = address
        self.line_1_number_building = line_1_number_building
        self.line_1_number_street = line_1_number_street
        self.line_1_area_locality = line_1_area_locality
        self.city = city
        self.zip_postcode = zip_postcode
        self.state_province_county = state_province_county
        self.country = country
        self.other_address_details = other_address_details

        #f"Customers('{self.address}', {self.line_1_number_building}, {self.line_1_number_street}, {self.line_1_area_locality}, {self.city}, {self.other_customer_details}, {self.zip_postcode}, {self.state_province_county}, {self.country}, {self.other_address_details})"

    def __repr__(self) -> str:
        return f"Item('{self.id}', {self.address}, {self.line_1_number_building}, {self.line_1_number_street}, {self.line_1_area_locality}, {self.city}, {self.zip_postcode}, {self.line_1_number_street}, {self.state_province_county}, {self.country}, {self.other_address_details})"
    def get_json(self):
        return self.__dict__
    def last_id(self):
        try:
            fp = open('Addresses.dat', 'r')
            x = fp.read()
            fp.close()
        except:
            fp = open('Addresses.dat', 'w')

        if x == "null" or x == "":
            fp = open('Addresses.dat', 'w')
            fp.write("[]")
            fp.close()
            fp = open('Addresses.dat', 'r')
            x = fp.read()
            fp.close()
        leggi = json.loads(x)
        last_id = len(leggi)
        return last_id

    def get_address(self):  #
        return self.address

    def set_address(self):  #
        self.address = input("mitti indirizzo: ")
        return self.address

    def get_line_1_number_building(self):
        return self.line_1_number_building

    def set_line_1_number_building(self, line_1_number_building):
        self.line_1_number_building = line_1_number_building

    def get_line_1_number_street(self):
        return self.line_1_number_street

    def set_line_1_number_street(self, line_1_number_street):
        self.line_1_number_street = line_1_number_street

    def get_line_1_area_locality(self):
        return self.line_1_area_locality

    def set_line_1_area_locality(self, line_1_area_locality):
        self.line_1_area_locality = line_1_area_locality

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_zip_postcode(self):
        return self.zip_postcode

    def set_zip_postcode(self, zip_postcode):
        self.zip_postcode = zip_postcode

    def get_state_province_county(self):
        return self.state_province_county

    def set_state_province_county(self, state_province_county):
        self.state_province_county = state_province_county

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_other_address_details(self):
        return self.other_address_details

    def set_other_address_details(self, other_address_details):
        self.other_address_details = other_address_details
