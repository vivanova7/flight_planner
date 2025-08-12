import sqlite3

import os
from datetime import datetime, timedelta

DATABASE = os.path.join(os.path.dirname(__file__), 'flight_planner.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

'''City CRUD operations'''

def create_city(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cities (name) VALUES (?)', (name,))
    conn.commit()
    city_id = cursor.lastrowid
    conn.close()
    return {'id': city_id, 'name': name}


def get_city(city_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cities WHERE id = ?', (city_id,))
    city = cursor.fetchone()
    conn.close()
    if city:
        return dict(city)


def delete_city(city_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cities WHERE id = ?', (city_id,))
    conn.commit()
    conn.close()


def get_all_cities():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cities')
    cities = cursor.fetchall()
    conn.close()
    return [dict(city) for city in cities]


def delete_all_cities():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cities')
    conn.commit()
    conn.close()


'''Airport CRUD operations'''

def create_airport(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO airports (name) VALUES (?)', (data['name']))
    conn.commit()
    airport_id = cursor.lastrowid
    conn.close()
    return {'id': airport_id, **data}


def get_airport(airport_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM airports WHERE id = ?', (airport_id,))
    airport = cursor.fetchone()
    conn.close()
    if airport:
        return dict(airport)


def update_airport(airport_id, name, city_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE airports SET name = ?, city_id = ? WHERE id = ?', (name, city_id, airport_id))
    conn.commit()
    conn.close()
    return {'id': airport_id, 'name': name, 'city_id': city_id}

def update_all_airports(data=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM cities ORDER BY id LIMIT 1')
    default_city_id = cursor.fetchone()
    if default_city_id:
        default_city_id = default_city_id[0]
    else:
        default_city_id = None
    if data and 'city_id' in data:
        city_id = data['city_id']
    else:
        city_id = default_city_id
    if city_id is not None:
        cursor.execute('''
            UPDATE airports 
            SET city_id = ?
            WHERE city_id IS NULL
        ''', (city_id,))
        conn.commit()
        cursor.execute('SELECT id, name, city_id FROM airports')
        updated_airports = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'city_id': row[2]} for row in updated_airports]
    else:
        conn.close()


def delete_airport(airport_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM airports WHERE id = ?', (airport_id,))
    conn.commit()
    conn.close()



def delete_all_airports():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM airports')
    conn.commit()
    conn.close()



def get_all_airports():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM airports')
    airports = cursor.fetchall()
    conn.close()
    return [dict(airport) for airport in airports]


'''Flight CRUD operations'''

def create_flight(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO flights (arrivalAirport, departureAirport, departureTime, travelTime, price) VALUES (?, ?, ?, ?, ?)''',
                   (data['arrivalAirport'], data['departureAirport'],  data['departureTime'],
                    data['travelTime'], data['price']))
    conn.commit()
    flight_id = cursor.lastrowid
    conn.close()
    return {'id': flight_id, **data}

def get_flight(flight_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM flights WHERE id = ?', (flight_id,))
    flight = cursor.fetchone()
    conn.close()
    if flight:
        return dict(flight)


def update_flight(flight_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE flights SET arrivalAirport = ?, departureAirport = ?, departureTime = ?, travelTime = ?, price = ? WHERE id = ?''',
                   (data['arrivalAirport'], data['departureAirport'], data['departureTime'],
                    data['travelTime'], data['price'], flight_id))
    conn.commit()
    conn.close()
    return {'id': flight_id, **data}


def delete_flight(flight_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM flights WHERE id = ?', (flight_id,))
    conn.commit()
    conn.close()


def get_all_flights(offset=0, max_count=50, sort_by='departureTime', sort_order='ASC'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM flights ORDER BY {sort_by} {sort_order} LIMIT ? OFFSET ?''',
                   (max_count, offset))
    flights = cursor.fetchall()
    conn.close()
    return [dict(flight) for flight in flights]


def delete_all_flights():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM flights')
    conn.commit()
    conn.close()

def search_flights(criteria):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''
        SELECT f.id, f.arrivalAirport, f.departureAirport, f.departureTime, f.travelTime, f.price
        FROM flights f
        JOIN airports dep_airport ON dep_airport.id = f.departureAirport
        JOIN airports arr_airport ON arr_airport.id = f.arrivalAirport
        JOIN cities dep_city ON dep_city.id = dep_airport.city_id
        JOIN cities arr_city ON arr_city.id = arr_airport.city_id
        WHERE dep_city.name = ? 
          AND arr_city.name = ?
          AND f.price BETWEEN ? AND ? 
          AND f.departureTime BETWEEN ? AND ?
          AND f.travelTime <= ?;
    '''

    params = (
        criteria['departureCity'],
        criteria['arrivalCity'],
        criteria['minPrice'],
        criteria['maxPrice'],
        criteria['minDepartureTime'],
        criteria['maxDepartureTime'],
        criteria['maxTravelTime'],
    )
    cursor.execute(query, params)
    flights = cursor.fetchall()
    filtered_flights = []
    for flight in flights:
        departure_time = flight[3]
        travel_time = flight[4]
        departure_dt = datetime.strptime(departure_time, "%H:%M")
        arrival_dt = departure_dt + timedelta(minutes=travel_time)
        arrival_time = arrival_dt.strftime("%H:%M")

        if 'minArrivalTime' in criteria:
            min_arrival_dt = datetime.strptime(criteria['minArrivalTime'], "%H:%M")
            if arrival_dt < min_arrival_dt:
                continue

        if 'maxArrivalTime' in criteria:
            max_arrival_dt = datetime.strptime(criteria['maxArrivalTime'], "%H:%M")
            if arrival_dt > max_arrival_dt:
                continue

        filtered_flights.append({
            'id': flight[0],
            'departureAirport': flight[1],
            'arrivalAirport': flight[2],
            'departureTime': departure_time,
            'travelTime': travel_time,
            'price': flight[5],
            'arrivalTime': arrival_time
        })

    conn.close()

    return filtered_flights



def connecting_flights(data):
    """
    Finds connecting flights matching the given criteria.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    query_departure = '''
        SELECT f.id AS first_flight_id, f.arrivalAirport, f.departureTime AS first_departure_time, 
               f.travelTime AS first_travel_time, f.price AS first_price
        FROM flights f
        JOIN airports dep_airport ON dep_airport.id = f.departureAirport
        JOIN airports inter_airport ON inter_airport.id = f.arrivalAirport
        JOIN cities dep_city ON dep_city.id = dep_airport.city_id
        JOIN cities inter_city ON inter_city.id = inter_airport.city_id
        WHERE dep_city.name = ? AND f.price BETWEEN ? AND ?
    '''
    cursor.execute(query_departure, (
        data['departureCity'],
        data['minPrice'],
        data['maxPrice']
    ))
    first_leg_flights = cursor.fetchall()

    query_arrival = '''
        SELECT f.id AS second_flight_id, f.departureAirport, f.departureTime AS second_departure_time, 
               f.travelTime AS second_travel_time, f.price AS second_price
        FROM flights f
        JOIN airports dep_airport ON dep_airport.id = f.departureAirport
        JOIN airports arr_airport ON arr_airport.id = f.arrivalAirport
        JOIN cities inter_city ON inter_city.id = dep_airport.city_id
        JOIN cities arr_city ON arr_city.id = arr_airport.city_id
        WHERE arr_city.name = ? AND f.price BETWEEN ? AND ?
    '''
    cursor.execute(query_arrival, (
        data['arrivalCity'],
        data['minPrice'],
        data['maxPrice']
    ))
    second_leg_flights = cursor.fetchall()

    connecting_flights = []
    for first_leg in first_leg_flights:
        first_arrival_time = datetime.strptime(first_leg['first_departure_time'], "%H:%M") + timedelta(
            minutes=first_leg['first_travel_time'])
        for second_leg in second_leg_flights:
            if first_leg['arrivalAirport'] == second_leg['departureAirport']:
                second_departure_time = datetime.strptime(second_leg['second_departure_time'], "%H:%M")
                layover_time = (second_departure_time - first_arrival_time).total_seconds() / 60

                if 'maxLayoverTime' in data and layover_time > data['maxLayoverTime']:
                    continue
                if 'minLayoverTime' in data and layover_time < data['minLayoverTime']:
                    continue

                connecting_flights.append({
                    'firstFlight': {
                        'id': first_leg['first_flight_id'],
                        'arrivalAirport': first_leg['arrivalAirport'],
                        'departureTime': first_leg['first_departure_time'],
                        'travelTime': first_leg['first_travel_time'],
                        'price': first_leg['first_price']
                    },
                    'secondFlight': {
                        'id': second_leg['second_flight_id'],
                        'departureAirport': second_leg['departureAirport'],
                        'departureTime': second_leg['second_departure_time'],
                        'travelTime': second_leg['second_travel_time'],
                        'price': second_leg['second_price']
                    },
                    'totalPrice': first_leg['first_price'] + second_leg['second_price'],
                    'layoverTime': layover_time
                })

    conn.close()

    return connecting_flights
