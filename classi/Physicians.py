from classi import Adresses


class Physicians:
    __id = 0  # PK
    __address = None
    __physician_details = ""

    def __init__(self, address, physician_details):
        self.__id = id(self)
        self.__address = address
        self.__physician_details = physician_details

    def get_json(self):
        Phy = {}
        address = {}
        for c in self.__dict__:
            Phy[c] = self.__dict__[c]
        for c in self.__address.__dict__:
            address[c] = self.__address.__dict__[c]
        Phy['address'] = address
        return Phy

    def set_json(self):
        pass

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_id(self):
        return self.__id  #

    def get_physician_details(self):
        return self.__physician_details

    def set_physician_details(self, physician_details):
        self.__physician_details = physician_details
