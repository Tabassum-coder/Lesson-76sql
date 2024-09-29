import pandas as pd
import sqlite3

database='database.sqlite'
conn=sqlite3.connect(database)
print("Connected Successfully")

#get tables
tables=pd.read_sql("""Select * from sqlite_master where type='table';""",conn)
print(tables)

#check for null values in table
WicketTaken=pd.read_sql("""Select * from Wicket_Taken;""",conn)
print(WicketTaken.head())

WicketTakenNull=pd.read_sql("""Select * from Wicket_Taken where Fielders IS NULL;""",conn)
print(WicketTakenNull)
