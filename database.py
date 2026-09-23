import sqlite3 as s
con=s.connect("mydata.db")
cur=con.cursor()
cur.execute("Create table emp(id int, name varchar(20))")

con.commit()
con.close()