import sqlite3
import csv

DB_FILE = 'flight_planner.db'

CSV_FILES = {
    'cities': 'data/cities.csv',
    'airports': 'data/airports.csv',
    'flights': 'data/flights.csv',
}

TABLE_COLUMNS = {
    'cities': ['id', 'name'],
    'airports': ['id', 'name', 'city_id'],
    'flights': ['id', 'arrivalAirport', 'departureAirport', 'departureTime', 'travelTime', 'price'],
}

def import_csv_to_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for table, csv_file in CSV_FILES.items():
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            columns = TABLE_COLUMNS[table]
            placeholders = ', '.join('?' * len(columns))
            insert_query = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})'
            for row in reader:
                values = [row[col] for col in columns]
                cursor.execute(insert_query, values)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    import_csv_to_db()
