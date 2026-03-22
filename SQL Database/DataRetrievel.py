import sqlite3
# Establish a connection and create a cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

#Exceute sql

cur.execute("SELECT * FROM 'ips' ORDER BY ASN")
print(cur.fetchall())

cur.execute("SELECT address, asn FROM 'ips' ORDER BY ASN")
print(cur.fetchall())

cur.execute("SELECT address, asn FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

cur.execute("SELECT address, asn FROM 'ips' where asn = 140")
print(cur.fetchall())

cur.execute("SELECT address, asn FROM 'ips' where asn < 300 and domain like '%sa'")
result = cur.fetchall()
print(result)

result2 = cur.fetchall()
print(result2)