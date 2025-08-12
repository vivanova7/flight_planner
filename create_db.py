import sqlite3


DATABASE = 'flight_planner.db'

def create_db():
    conn = sqlite3.connect('flight_planner.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS airports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        city_id INTEGER,
                        FOREIGN KEY(city_id) REFERENCES cities(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        arrivalAirport INTEGER,
                        departureAirport INTEGER,
                        departureTime TIMESTAMP,
                        travelTime INTEGER,
                        price INTEGER,
                        FOREIGN KEY(departureAirport) REFERENCES airports(id),
                        FOREIGN KEY(arrivalAirport) REFERENCES airports(id))''')

    conn.commit()
    conn.close()


create_db()