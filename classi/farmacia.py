import Adresses
class Addresses:
    address_id = ""  # PK
    line_1_number_building = ""
    line_1_number_street = ""
    line_1_area_locality = ""
    city = ""
    zip_postcode = ""
    state_province_county = ""
    country = ""
    other_address_details = ""
class Customers:
    customer_id = "" #FK
    address_id = None
    customer_name = ""
    date_became_customer = ""
    credit_card_number = ""
    card_expiry_date = ""
    other_customer_details = ""
class Physicians:
    address_id = None
    physician_id = "" #PK
    physician_details = ""

class Prescription_items:
    prescription_id = "" #PF
    drug_id = ""  #PF
    prescription_quantity = ""
    instructions_to_customer = ""
class Ref_Prescription_Status:
    prescription_status_code = "" #PK
    prescription_status_description = ""
    # eg Filled, Part-Filled
    # eg Filled but not collected
class Ref_Payment_Methods:
    payment_method_code = ""  #PK
    payment_method_description = ""
    # eg Cash, Credit Card
class Prescriptions:
    customer_id = None
    physician_id = None
    payment_method_code = None
    prescription_status_code = None
    prescription_id = 0 #FK
    prescription_issued_date = "" #*
    prescription_filled_date = ""
    other_details = ""
class Drug_Companies:
    company_id = "" #PK
    company_name = ""
    other_company_details = ""

class Drugs_and_Medication:
    company_id = None
    drug_id = "" #PK
    drug_name = ""
    drug_cost = ""
    drug_available_date = "" #*
    drug_withdrawn_date = ""
    drug_description = ""
    generic_yn = ""
    generic_equivalent_drug_id = ""
    other_drug_details = ""