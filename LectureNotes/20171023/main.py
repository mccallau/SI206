import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')

cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)', ('Billy', 14))
cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)',('Billy', 15))
cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)',('Billy', 16))
cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)',('Billy', 17))
cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)',('Billiam', 20))

conn.commit()
for row in cur: 
	print(row)
	break
conn.close()



# Code: http://www.pythonlearn.com/code3/db1.py
# Or select Download from this trinket's left-hand menu