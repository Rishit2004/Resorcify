import os
import pandas as pd
import mysql.connector
import random as rand

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='ritu12345',
    database='resorcify'
)

sql= "select * from employee;"
mycursor=mydb.cursor()
mycursor.execute(sql)
myresult=mycursor.fetchall()
print(myresult)


df= pd.DataFrame()
for x in myresult:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('templates/sql-data.html')
