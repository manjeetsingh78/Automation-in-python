import sqlite3
import pandas

con = sqlite3.connect('database.db')
cur = con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn",con)
print(df)

# df.to_csv('database.csv',index=None)
# if we are using pandas then we should use pandas read sql function instead of cursor fetch all
df.to_excel('database.xlsx',index=None)