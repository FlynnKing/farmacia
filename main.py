from unittest import TextTestResult
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

# non trovo più lo schema database dei collegamenti, quindi mi limiterò a creare solo due oggetti comunicanti
# per poi salvarli


# oggetto salva oggetti
salva = PersistenceFactory()

# oggetto
indirizzo = Addresses("address", 23, 234, "Pescara", "Pescara", "923492378", "Via del giocattolo", "Europa", "other_address_details")

# oggetto contenente un altro oggetto
costume = Customers("Paolo", "DateTime", "inserimento di una data", "card_expiry_date", "other_customer_details", indirizzo)

# salvo oggetto
salva.get_persistence("file", indirizzo.get_json())

# salvo oggetto contenente un altro oggetto
salva.get_persistence("file", costume.get_json())

#costume.modifica("address", indirizzo)