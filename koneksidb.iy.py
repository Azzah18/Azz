# python implementation to bcreate a Database in MySQL
import mysql.connector 

# connecting to the mysql server
db = mysq.connetor.connect(
    host="localhost",
    user="root",
    passwd=""
)

# cursor object c
c = db.cursor()

# executing the create database statement 
c.execute("CREATE DATABASE db_sekolah")

# fetching all the database
c.execute("SHOW DATABASES")

# printing all the databases
for i in c:
    print(i)
c = db.cursor()

# finally closing the database connecting
db.close()