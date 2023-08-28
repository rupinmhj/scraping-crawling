import sqlite3

conn=sqlite3.connect('myquotes.db')
cur=conn.cursor()
cur.execute("""INSERT INTO quotes_table VALUES("Learning python","Rupin","Study smart")""")

# cur.execute("""create table quotes_table(
#             title varchar(20),
#             author varchar(20),
#             tag varchar(30))"""
# )

conn.commit()
conn.close()