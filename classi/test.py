
import mysql.connector
print('')
print('')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"

)

print('connessione al database, prima del cursor (puntatore): '+str(mydb))
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE sas (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
print('')
print('')