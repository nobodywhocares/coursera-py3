import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# fname = input('Enter file name: ')
# if len(fname) < 1:
fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

#    print(entry)
    name = entry[0]
    title = entry[1]
    role = entry[2]
#    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, int(role) ) )

conn.commit()

results = cur.execute('''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')
for result in results:
    print(result)
results = cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;''')
for result in results:
    print(result)
cur.close()
conn.close()

abc = "With three words"
stuff = abc.split()
print(stuff)
abc = "With three words"
stuff = abc.split()
print(len(stuff))

zap = "hello there bob"
print(zap[4])

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()

# ERROR at print("smuller") because no ident
# x = 12
# if x < 5:
# print("smaller")
# else:
#     print("bigger")
# print("all done")

stuff = ['joseph', 'sally', 'walter', 'tim']
print(stuff[2])

def hello():
    print("Hello")
    print("There")
x = 10
x = x + 1

x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value > x :
        x = value
print(x)

total = 0
for abc in range(5):
    total = total + abc
print(total)

a = "123"
b = 456
c = a + b
print(c)

line1
try:
     line2
     line3
     line4
except:
     line5
line6
