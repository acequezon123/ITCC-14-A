# ITCC-14-A
# Shoe APi


This is a simple Flask API for managing shoe data. It supports operations such as retrieving all shoes, retrieving a shoe by ID, adding a new shoe, filtering shoes by release date, searching for shoes by brand name, and updating a shoe by ID.

The API will be accessible at http://127.0.0.1:5000/.
# Endpoints
Get All Shoes
* Endpoint: /shoes
* Method: GET 
>Description: Get information about all shoes.
> 

Get Shoe by ID
* Endpoint: /shoes/<int:shoeId>
* Method: GET
>Description: Get information about a specific shoe by ID.

Add New Shoe
* Endpoint: /shoes
* Method: POST
>Description: Add a new shoe to the database.

Filter Shoes by Release Date
* Endpoint: /shoes/filter
* Method: GET
>Description: Get shoes filtered by release date.

Search Shoes by Brand Name
* Endpoint: /shoes/search
* Method: GET
>Description: Search for shoes by brand name.

Update Shoe by ID
* Endpoint: /shoes/<int:shoeId>
* Method: PUT
> Description: Update a specific shoe by ID.


Import the provided Postman collection: Shoe API Postman Collection.
Use the imported collection to test different API endpoints.
