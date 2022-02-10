from classi import Adresses


class Physicians:
    id = 0  # PK
    address = None
    physician_details = ""

    def __init__(self, lastid, physician_details):
        self.id = lastid + 1
        self.address = Adresses.Addresses
        self.physician_details = physician_details

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_id(self):
        return self.id  #

    def get_physician_details(self):
        return self.physician_details

    def set_physician_details(self, physician_details):
        self.physician_details = physician_details
