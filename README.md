A simple flight planning application with RESTful API endpoints for managing cities, airports, flights, and connecting flights.
Features
•	Manage cities, airports, flights, and connecting flights.
•	Supports data persistence in files or an SQL database.
•	RESTful API with endpoints for CRUD operations.

API Endpoints
City Endpoints
•	POST /cities/ - Create a new city
•	GET /cities/ - Get all cities
•	DELETE /cities/ - Delete all cities
•	GET /cities/<id> - Get a city by ID
•	DELETE /cities/<id> - Delete a city by ID
Airport Endpoints
•	POST /airports/ - Create a new airport
•	PUT /airports/ - Edit the whole collection of airports
•	DELETE /airports/ - Delete all airports
•	GET /airports/ - Get a collection of airports
•	GET /airports/<id> - Get an airport by ID
•	DELETE /airports/<id> - Delete an airport by ID
Flight Endpoints
•	POST /flights/ - Create a new flight
o	Request body example:
o	{
o	  "arrivalAirport": 27,
o	  "departureAirport": 2,
o	  "departureTime": "12:35",
o	  "travelTime": 45,
o	  "price": "$300"
}
•	GET /flights/ - Get all flights with optional query parameters for pagination and sorting
o	Query parameters:
	offset (default: 0) - The starting point for the list of flights
	maxCount (default: 50) - The maximum number of flights to return
	sortBy (default: "departureTime") - The field to sort by
	sortOrder (default: "ASC") - The order of sorting (ASC or DESC)
•	POST /flights/search - Search for flights based on criteria
o	Request body example:
o	{
o	  "departureCity": "New York",
o	  "arrivalCity": "Los Angeles",
o	  "minPrice": 100,
o	  "maxPrice": 500,
o	  "minDepartureTime": "08:00",
o	  "maxDepartureTime": "20:00",
o	  "maxTravelTime": 300,
o	  "minArrivalTime": "10:00",
o	  "maxArrivalTime": "22:00"
}
•	GET /flights/<id> - Get a flight by ID
•	PUT /flights/<id> - Edit a flight by ID
•	DELETE /flights/<id> - Delete a flight by ID
