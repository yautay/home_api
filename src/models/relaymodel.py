import sqlite3


class RelayModel:
    def __init__(self, _id, name, state, timestamp):
        self.id = _id
        self.name = name
        self.state = state
        self.timestamp = timestamp

    def json(self):
        json = {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "timestamp": self.timestamp
        }
        return json

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM relays WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row:
            return cls(row[0], row[1], row[2], row[3])

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO relays VALUES (NULL , ?, ?, ?)"
        cursor.execute(query, (self.name, self.state, self.timestamp,))
        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE relays SET state=?, timestamp=? WHERE name=?"
        cursor.execute(query, (self.state, self.timestamp, self.name))
        connection.commit()
        connection.close()
