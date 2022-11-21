import sqlite3

from work2 import final


final2 = []
for i in range(len(final)):
    final2.append(tuple(final[i].values()))

final3 = [('Banahaha', 'Boku no Hero Academia', 'Sora ni Utaeba', 'amazarashi', 'Opening 2', 'https://files.catbox.moe/k0myox.webm', 'https://files.catbox.moe/u09jit.mp3'),('Burning Kabaddi', 'Shakunetsu Kabaddi', 'FIRE BIRD', 'Shunya Ōhira', 'Opening 1', 'https://files.catbox.moe/sdtehr.webm', 'https://files.catbox.moe/gdejwk.mp3')]

conn = sqlite3.connect('text.db') # connection (creates) to database

c = conn.cursor() # to start sql commands


#NULL, INTEGER, 

# c.execute("""
#     CREATE TABLE GRAPE (
#     title VARCHAR,
#     titleRom VARCHAR, 
#     song VARCHAR,
#     artist VARCHAR,
#     opedin VARCHAR,
#     video VARCHAR,
#     audio VARCHAR,
#     un_min text GENERATED ALWAYS AS (MIN(title, titleRom, song, artist, opedin)),
#     un_max text GENERATED ALWAYS AS (MAX(title, titleRom, song, artist, opedin)),
#     UNIQUE(un_min, un_max));
# """)

# sql = """INSERT OR IGNORE INTO grape 
# (title, titleRom, song, artist, opedin, video, audio) 
# VALUES (?, ?, ?, ?, ?, ?, ?);"""

# c.executemany(sql, final2[:5])


# sql = """INSERT OR IGNORE INTO grape 
# (title, titleRom, song, artist, opedin, video, audio) 
# VALUES (?, ?, ?, ?, ?, ?, ?);"""

# c.executemany(sql, final3)

# c.execute("""DROP TABLE BANANA""")

# c.execute("""DELETE FROM BANANA WHERE ROWID <=20""")

# sql = ("""
# INSERT OR IGNORE INTO BANANA (title, titleRom, song, artist, opedin, video, audio) 
# VALUES (?, ?, ?, ?, ?, ?, ?)
# """)

# c.executemany(sql, final2[:2])

# x = c.execute("""SELECT un_min FROM GRAPE WHERE ROWID<6""")
# for i in x:
#     print(i)

conn.commit()
