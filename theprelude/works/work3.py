import sqlite3

from work2 import final

try:
    conn = sqlite3.connect('the.db')
    sql = """
    CREATE TABLE PAP (
    title VARCHAR,
    titleRom VARCHAR, 
    song VARCHAR,
    artist VARCHAR,
    opedin VARCHAR,
    video VARCHAR,
    audio VARCHAR
    );
    """
    # sql = """INSERT INTO AYAYA
    # (title, titleRom, song, artist, opedin, video, audio)
    # VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor = conn.cursor()
    cursor.executemany(sql, final)
    conn.commit()
    print("Multiple Insert Operation OK")
    cursor.close()

except sqlite3.Error as e:
    print("Connection Error: ", e)

finally:
    if (conn):
        conn.close()
        print("Connection Closed")
