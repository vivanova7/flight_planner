import unittest
from unittest.mock import patch, MagicMock
from flight_planner.services import CityService, AirportService, FlightService


# FILE: flight_planner/test_services.py

class SmartTestCase(unittest.TestCase):
    def assertIncludes(self, actual, expected):
        for key, value in expected.items():
            self.assertEqual(actual[key], value)

    def assertPiecewiseIncludes(self, actual, expected):
        if len(actual) != len(expected):
            self.fail('Length mismatch')
        for (item, reference) in zip(actual, expected):
            self.assertIncludes(item, reference)


class TestCityService(SmartTestCase):

    @patch('flight_planner.services.storage')
    def test_create_city(self, mock_storage):
        mock_storage.create_city.return_value = {'id': 1, 'name': 'Test City'}
        response = CityService.create_city({'name': 'Test City'})
        self.assertIncludes(response, {'id': 1, 'name': 'Test City'})

    @patch('flight_planner.services.storage')
    def test_get_all_cities(self, mock_storage):
        mock_storage.get_all_cities.return_value = [{'id': 1, 'name': 'Test City'}]
        response = CityService.get_all_cities()
        self.assertPiecewiseIncludes(response, [{'id': 1, 'name': 'Test City'}])

    @patch('flight_planner.services.storage')
    def test_get_city(self, mock_storage):
        mock_storage.get_city.return_value = {'id': 1, 'name': 'Test City'}
        response = CityService.get_city(1)
        self.assertIncludes(response, {'id': 1, 'name': 'Test City'})

    @patch('flight_planner.services.storage')
    def test_get_city_not_found(self, mock_storage):
        mock_storage.get_city.return_value = None
        with self.assertRaises(KeyError) as context:
            CityService.get_city(1)

    @patch('flight_planner.services.storage')
    def test_delete_city(self, mock_storage):
        response = CityService.delete_city(1)
        self.assertEqual(response, '')

    @patch('flight_planner.services.storage')
    def test_delete_all_cities(self, mock_storage):
        response = CityService.delete_all_cities()
        self.assertEqual(response, '')


class TestAirportService(SmartTestCase):

    @patch('flight_planner.services.storage')
    def test_create_airport(self, mock_storage):
        mock_storage.create_airport.return_value = {'id': 1, 'name': 'Test Airport'}
        response = AirportService.create_airport({'name': 'Test Airport'})
        self.assertIncludes(response, {'id': 1, 'name': 'Test Airport'})

    @patch('flight_planner.services.storage')
    def test_get_all_airports(self, mock_storage):
        mock_storage.get_all_airports.return_value = [{'id': 1, 'name': 'Test Airport'}]
        response = AirportService.get_all_airports()
        self.assertPiecewiseIncludes(response, [{'id': 1, 'name': 'Test Airport'}])

    @patch('flight_planner.services.storage')
    def test_get_airport(self, mock_storage):
        mock_storage.get_airport.return_value = {'id': 1, 'name': 'Test Airport'}
        response = AirportService.get_airport(1)
        self.assertIncludes(response, {'id': 1, 'name': 'Test Airport'})

    @patch('flight_planner.services.storage')
    def test_get_airport_not_found(self, mock_storage):
        mock_storage.get_airport.return_value = None
        with self.assertRaises(KeyError) as context:
            AirportService.get_airport(1)

    @patch('flight_planner.services.storage')
    def test_delete_airport(self, mock_storage):
        response = AirportService.delete_airport(1)
        self.assertEqual(response, '')

    @patch('flight_planner.services.storage')
    def test_delete_all_airports(self, mock_storage):
        response = AirportService.delete_all_airports()
        self.assertEqual(response, '')


class TestFlightService(SmartTestCase):

    @patch('flight_planner.services.storage')
    def test_create_flight(self, mock_storage):
        mock_storage.create_flight.return_value = {'id': 1, 'name': 'Test Flight'}
        response = FlightService.create_flight({'name': 'Test Flight'})
        self.assertIncludes(response, {'id': 1, 'name': 'Test Flight'})

    @patch('flight_planner.services.storage')
    def test_get_all_flights(self, mock_storage):
        mock_storage.get_all_flights.return_value = [{'id': 1, 'name': 'Test Flight'}]
        response = FlightService.get_all_flights()
        self.assertPiecewiseIncludes(response, [{'id': 1, 'name': 'Test Flight'}])

    @patch('flight_planner.services.storage')
    def test_get_flight(self, mock_storage):
        mock_storage.get_flight.return_value = {'id': 1, 'name': 'Test Flight'}
        response = FlightService.get_flight(1)
        self.assertIncludes(response, {'id': 1, 'name': 'Test Flight'})

    @patch('flight_planner.services.storage')
    def test_get_flight_not_found(self, mock_storage):
        mock_storage.get_flight.return_value = None
        with self.assertRaises(KeyError) as context:
            FlightService.get_flight(1)

    @patch('flight_planner.services.storage')
    def test_delete_flight(self, mock_storage):
        response = FlightService.delete_flight(1)
        self.assertEqual(response, '')

    @patch('flight_planner.services.storage')
    def test_delete_all_flights(self, mock_storage):
        response = FlightService.delete_all_flights()
        self.assertEqual(response, '')


if __name__ == '__main__':
    unittest.main()