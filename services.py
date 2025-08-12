import flight_planner.storage as storage



class CityService:
    """This class handle city-related CRUD operations."""
    @staticmethod
    def create_city(data):
        return storage.create_city(data['name'])

    @staticmethod
    def get_city(city_id):
        city = storage.get_city(city_id)
        if not city:
            raise KeyError
        return city

    @staticmethod
    def get_all_cities():
        return storage.get_all_cities()


    @staticmethod
    def delete_city(city_id):
        storage.delete_city(city_id)
        return ''

    @staticmethod
    def delete_all_cities():
        storage.delete_all_cities()
        return ''


class AirportService:
    """This class handle airport-related CRUD operations."""

    @staticmethod
    def create_airport(data):
        return storage.create_airport(data)

    @staticmethod
    def get_all_airports():
        return storage.get_all_airports()

    @staticmethod
    def get_airport(airport_id):
        airport = storage.get_airport(airport_id)
        if not airport:
            raise KeyError
        return airport

    @staticmethod
    def update_airport(airport_id, data):
        return storage.update_airport(airport_id, data['name'], data['city_id'])

    @staticmethod
    def delete_airport(airport_id):
        storage.delete_airport(airport_id)
        return ''

    @staticmethod
    def delete_all_airports():
        storage.delete_all_airports()
        return ''

    @staticmethod
    def update_all_airports(data=None):
        return storage.update_all_airports(data)

class FlightService:
    """This class handle flight-related CRUD operations."""
    @staticmethod
    def create_flight(data):
        return storage.create_flight(data)

    @staticmethod
    def get_all_flights(offset=0, max_count=50, sort_by='departure_time', sort_order='ASC'):
        return storage.get_all_flights(offset, max_count, sort_by, sort_order)

    @staticmethod
    def get_flight(flight_id):
        flight = storage.get_flight(flight_id)
        if not flight:
            raise KeyError
        return flight

    @staticmethod
    def update_flight(flight_id, data):
        return storage.update_flight(flight_id, data)

    @staticmethod
    def delete_flight(flight_id):
        storage.delete_flight(flight_id)
        return ''

    @staticmethod
    def delete_all_flights():
        storage.delete_all_flights()
        return ''

    @staticmethod
    def search_flights(criteria):
        return storage.search_flights(criteria)


    @staticmethod
    def connecting_flights(data):
        return storage.connecting_flights(data)




