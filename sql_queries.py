import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM artists")

data = cursor.fetchall()
# Запитання 1. Інформація про скількох художників представлена у базі даних?
print(len(data))

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('''SELECT * FROM artists WHERE "Gender"=="Female"''')
data = cursor.fetchall()
print(len(data))


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('''SELECT * FROM artists WHERE "Birth Year" < 1900''')
data = cursor.fetchall()
print(len(data))


# Запитання 4*. Як звати найстаршого художника?
cursor.execute('''SELECT * FROM artists ORDER BY "Birth Year" ''')
data = cursor.fetchone()
print(data)

cursor.execute('''INSERT INTO artists("Artist ID", "Name","Nationality", "Gender", "Birth Year") VALUES((?), (?), (?), (?), (?))''', [650 , "Van goh", "netherlands", "male", 1853])
conn.commit()




cursor.close()
conn.close()