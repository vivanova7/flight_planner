✈️ Flight Planning API

A simple RESTful application for managing cities, airports, flights, and connecting flights. Supports persistent storage using files or SQL databases.

🚀 API Endpoints

🏙️ City Endpoints
Method	Endpoint	Description

POST	/cities/	Create a new cityn/GET	/cities/	Get all cities

DELETE	/cities/	Delete all cities

GET	/cities/<id>	Get a city by ID

DELETE	/cities/<id>	Delete a city by ID


🛫 Airport Endpoints
Method	Endpoint	Description
POST	/airports/	Create a new airport
PUT	/airports/	Edit the entire airport list
DELETE	/airports/	Delete all airports
GET	/airports/	Get all airports
GET	/airports/<id>	Get an airport by ID
DELETE	/airports/<id>	Delete an airport by ID

✈️ Flight Endpoints
Method	Endpoint	Description
POST	/flights/	Create a new flight
GET	/flights/	Get all flights (supports pagination & sorting)
POST	/flights/search	Search for flights
GET	/flights/<id>	Get a flight by ID
PUT	/flights/<id>	Edit a flight by ID
DELETE	/flights/<id>	Delete a flight by ID

📌 Features
Manage cities, airports, flights, and connecting flights
RESTful API with full CRUD operations
Search and filter flights with various criteria
Supports pagination, sorting, and data persistence

💾 Data Persistence
This application supports:
Saving data to files
Connecting to an SQL database
