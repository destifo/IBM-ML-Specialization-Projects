import sqlite3 as sq
import pandas as pd
import pandas.io.sql as pds

fpath = 'data/classic_rock.db'
conn = sq.Connection(fpath)
cur = conn.cursor()

cur.execute('show tables')
data = pds.read_sql('SELECT * FROM rock_songs;', conn)
print(data.head())
print(data.iloc[:5])