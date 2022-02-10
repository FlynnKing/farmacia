from classi import Adresses
import json

class Persistence:
    def __init__(self):
        self.save()

    def save(self):
        return print('save data from ' + str(type(self)))


class DBPersistence(Persistence):  # db
    def save(self):
        print('Salvo sul database generico')


class RamPersistence(Persistence):  # RAM
    def save(self):
        # l'ogetto passato viene salavto dentro una lista
        lista_oggetti = []
        print('salvo su RAM')


class FilePersistence(Persistence):  # File
    def __init__(self, oggetto):
        self.dati_salvati = self.upload(oggetto)
        self.save(self.dati_salvati)
    def save(self, oggetto):
        diz = []
        for attr in oggetto.__dict__:
            stringa = "["
    def upload(self, oggetto):
        def save_on_txt():
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
            return leggi
        dict = []
        print('salvo su MySQL:')
        for attr in oggetto.__dict__:
            dict.append(attr)
            print(attr)
        print(dict)
    


class MysqlDatabase(DBPersistence):  # Myql
    def __init__(self):
        self.save()
    def save(self):
        # l'ogetto passato viene salavto su un db

        print('salvo su db')



#  oggetto.__class__.__name__
# ---------------------------------------------------------------------------------------
class DB2Database(DBPersistence):
    def __init__(self):
        self.save()

    def save(self):
        return print('salvo su DB2')


class PGDatabase(DBPersistence):  # PGD
    def __init__(self):
        self.save()

    def save(self):
        return print('salvo su Postgresql')


class MSSQLDatabase(DBPersistence):
    def __init__(self):
        self.save()

    def save(self):
        return print('salvo su SQL SERVER')


class PersistenceFactory():

    def get_persistence(self, persistence_type, pers_obj):
        oggetto = pers_obj
        params = persistence_type.split(',')
        type_pers = len(params)
        if type_pers == 1:
            if persistence_type == "ram":
                RamPersistence.save(oggetto)
            elif persistence_type == "file":
                obj = FilePersistence(oggetto)
                obj.save(oggetto)
            else:
                print("pers_obj = None")
        else:
            if params[0] == "db":
                if params[1] == 'mysql':
                    MysqlDatabase(oggetto)
                    #ok.save(oggetto)
                elif (params[1] == 'mssql'):
                    MSSQLDatabase.save(oggetto)
                elif (params[1] == 'pgsql'):
                    PGDatabase.save(oggetto)
                elif (params[1] == 'db2'):
                    DB2Database.save(oggetto)
                else:
                    print("pers_obj = None")
            else:
                print("pers_obj = None")
