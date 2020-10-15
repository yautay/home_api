import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS relays (id INTEGER PRIMARY KEY, name text, state integer, timestamp text)"
cursor.execute(create_table)
insert_test_relay = "INSERT INTO relays VALUES (1, 'test', 1, '2020-10-12')"
cursor.execute(insert_test_relay)


connection.commit()
connection.close()
