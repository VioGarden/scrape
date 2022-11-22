import sqlite3

from work2 import final


final2 = []
for i in range(len(final)):
    final2.append(tuple(final[i].values()))

conn = sqlite3.connect('text.db') # connection (creates) to database

c = conn.cursor() # to start sql commands

#NULL, INTEGER, 

# c.execute("""
#     CREATE TABLE BANANA (
#     title VARCHAR,
#     titleRom VARCHAR, 
#     annid INT,
#     song VARCHAR,
#     artist VARCHAR,
#     opedin VARCHAR,
#     video VARCHAR,
#     audio VARCHAR);
# """)

# sql = """INSERT INTO banana 
# (title, titleRom, song, artist, opedin, video, audio) 
# VALUES (?, ?, ?, ?, ?, ?, ?);"""

# c.executemany(sql, final2[:3])

# c.execute("""DROP TABLE BANANA""")

# c.execute("""DELETE FROM BANANA WHERE ROWID <=20""")

# sql = ("""
# INSERT OR IGNORE INTO BANANA (title, titleRom, song, artist, opedin, video, audio) 
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """)

# c.executemany(sql, final2[:2])

# x = c.execute("""SELECT song, title FROM BANANA WHERE ROWID<5""")
# for i in x:
#     print(i)

conn.commit()

conn.close()


