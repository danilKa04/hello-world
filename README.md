import sqlite3 as sq
    
with sq.connect('users.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE  IF NOT EXISTS users(
    chat_id INTEGER,
    user_id INTEGER,	
    first_name TEXT,
    second_name TEXT,
    nick TEXT,
    money INTEGER DEFAULT 0
    )""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")

print ("""post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ID TEXT NOT NULL,
    name TEXT NOT NULL,
    """);

print ("""
INSERT INTO comments ('ID, 1')
VALUES ('name, Нечитаемые/поврежденные дорожные знаки')
""");

print ("""
INSERT INTO comments ('ID, 2')
VALUES ('name, Противоречие при установке дорожных знаков/разметки/светофора, неправильно установленные дорожные знаки/разметка/светофор')
""");

print ("""
INSERT INTO comments ('ID, 3')
VALUES ('name, Стертая дорожная разметка')
""");

print ("""
INSERT INTO comments ('ID, 4')
VALUES ('name, Неисправное уличное освещение')
""");

print ("""
INSERT INTO comments ('ID, 5')
VALUES ('name, Неисправное освещение во дворах')
""");

print ("""
INSERT INTO comments ('ID, 6')
VALUES ('name, Неисправное освещение в парках')
