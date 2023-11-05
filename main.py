import sqlite3
import pandas as pd

conn = sqlite3.connect('high_freq.db')
df = pd.read_sql('select * from zhangtinggu',conn)
print(df)
conn.close()