#specifiche connessione al database mysql e sqlite
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)

import sqlite3

connessione=sqlite3.connect("C:\\Users\\necci\\OneDrive\\Desktop\\Gestione_Libri.db")
print("connesso!!")
