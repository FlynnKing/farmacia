from classi.Adresses import Addresses
from datetime import datetime
import time
from classi.Customers import Customers
from classi.Drug_Companies import Drug_Companies
from classi.Drugs_and_Medication import Drugs_and_Medication
from classi.Persistenza import PersistenceFactory
from classi.Physicians import Physicians
from classi.Prescriptions import Prescriptions
from classi.Prescription_items import Prescription_items
from classi.Ref_Prescription_Status import Ref_Prescription_Status
from classi.Ref_Payment_Methods import Ref_Payment_Methods

salva = PersistenceFactory()

# CREA L'OGETTO COMPLETO RISPETTANDO LE ENTITA'

indirizzo = Addresses("address",23, 234, "Pescara", "Pescara", "923492378", "Via del giocattolo", "Europa", "other_address_details")
print(indirizzo)
costume = Customers(823546234, "Paolo", "DateTime", "inserimento di una data" , "card_expiry_date","other_customer_details", indirizzo.get_json())
print("")
print(costume)
salva.get_persistence("file", costume)
#for attr in p.__dict__:
#    print(


# crea_indirizzo = Addresses.set_address()
# crea_indirizzo.save_all(crea_indirizzo)

# @staticmetod #non passa per __init__
# a = property(__get__a, __set__a) # get accede alla variabile, poi set 
# @a.setter #se stai per modificare a passa per di qua
# def ...
# @property #oscura la classe a chi la sta utilizzando, in imput prende 4 parametri al massimo, principalmente (__get__a, __set__a)
# 