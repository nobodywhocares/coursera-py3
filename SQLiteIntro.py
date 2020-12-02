import sqlite3

dbconn = sqlite3.connect('dbintro.sqlite3')
dbcur = dbconn.cursor()

dbcur.execute("DROP TABLE IF EXISTS Ages")
dbcur.execute("""CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)""")
dbconn.commit()
dbcur.executescript("""DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Kellen', 13);
INSERT INTO Ages (name, age) VALUES ('Megan', 14);
INSERT INTO Ages (name, age) VALUES ('Maeve', 30);
INSERT INTO Ages (name, age) VALUES ('Pola', 37);
""")
dbconn.commit()
results = dbcur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X").fetchone()
print(results)

dbcur.close();