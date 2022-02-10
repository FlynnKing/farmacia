import json
import mysql.connector


class Persistence:
    def __init__(self):
        self.save()

    def save(self):
        return print('save data from ' + str(type(self)))


class DBPersistence(Persistence):  # db
    def __init__(self):
        self.save()

    def save(self):
        print('Salvo sul database generico')


class RamPersistence(Persistence):  # RAM
    def save(self):
        # l'ogetto passato viene salavto dentro una lista
        lista_oggetti = []
        print('salvo su RAM')


class FilePersistence(Persistence):  # File

    def __init__(self, oggetto):
        self.upload(oggetto)

    def upload(self, oggetto):

        def save_on_txt():  # funzione per perndere l'elenco degli oggetti/dizionari
            try:
                fp = open("tutto.dat", 'r')
                x = fp.read()
                fp.close()
            except:
                fp = open("tutto.dat", 'w')
                fp.write('[]')
                fp.close()
            if x == "null" or x == "":
                fp = open("tutto.dat", 'w')
                fp.write('[]')
                fp.close()
                fp = open("tutto.dat", 'r')
                x = fp.read()
                fp.close()
            print(x)
            leggi = json.loads(x)
            return leggi

        lista_dizionari = save_on_txt()
        lista_dizionari.append(oggetto)

        def scrivi(dizionario):
            fp = open("tutto.dat", 'w')
            fp.write(json.dumps(dizionario))
            fp.close()

        scrivi(lista_dizionari)


class MysqlDatabase(DBPersistence):  # Myql
    def __init__(self):
        self.save()

    def save(self):
        # UTILIZZO MYSQL

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
                FilePersistence(oggetto) ######
                
            else:
                print("Nonee")
        else:
            if params[0] == "db":
                if params[1] == 'mysql':
                    MysqlDatabase(oggetto)
                    # ok.save(oggetto)
                elif (params[1] == 'mssql'):
                    MSSQLDatabase.save(oggetto)
                elif (params[1] == 'pgsql'):
                    PGDatabase.save(oggetto)
                elif (params[1] == 'db2'):
                    DB2Database.save(oggetto)
                else:
                    print("NONE")
            else:
                print("nononone")
