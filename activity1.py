import pandas as pd
import sqlite3

database='database.sqlite'
conn=sqlite3.connect(database)
print("Connected Successfully")

# conn.execute("""CREATE TABLE EMPLOYES (
#              SNO INT PRIMARY KEY,
#              EMP_ID INT NOT NULL,
#              EMP_NAME TEXT NOT NULL,
#              CONTACTNO INT NOT NULL,
#              CITY TEXT NOT NULL );""")
# print("table created successfully")

# conn.execute("INSERT INTO EMPLOYES(SNO,EMP_ID,EMP_NAME,CONTACTNO,CITY)\
#              VALUES(1,1,'ALI',6678964345,'BANGALORE')")
# conn.execute("INSERT INTO EMPLOYES(SNO,EMP_ID,EMP_NAME,CONTACTNO,CITY)\
#              VALUES(2,2,'MUFADDAL',6678964345,'HYDERABAD')")
# conn.commit()
# print("records inserted successfully")

EMPtable=pd.read_sql("""Select * from EMPLOYES ;""",conn)
print(EMPtable)