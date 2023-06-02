import mysql.connector


print(' ')

mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="example"
)

cursor = mydb.cursor()

if (mydb.is_connected()):
    print("Connected\n")
else:
    print("Not connected\n")

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
# print(databases)

## showing one by one database
for database in databases:
    print(database)
    
print('\n-----------------------------\n')

cursor.execute("USE mydatabase")
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)