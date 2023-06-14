import requests
import json
import random


# Validate GET request for all locations using /locations endpoint
def test_1_validate_objects_returned():
    response = requests.get("http://127.0.0.1:8000/locations")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response_body, list)
    print(response_body)


# Validate POST request for new location creation using /locations endpoint
def test_2_validate_object_creation():
    url = "http://127.0.0.1:8000/locations"
    newObject = {
        "id": random.randint(10000, 99999),  # Creates a new location with the following attributes
        "city": "Denver AUTOMATED (POST)",
        "country": "United States AUTOMATED (POST)",
    }
    postObject = requests.post(url, json=newObject)
    response_body = postObject.json()
    print(response_body)
    new_location_id = response_body["id"]
    print(new_location_id)
    assert response_body["id"] == new_location_id
    assert response_body["city"] == "Denver AUTOMATED (POST)"
    assert response_body["country"] == "United States AUTOMATED (POST)"
    print(response_body)


# Validate PATCH request for updating a location record using /location endpoint
def test_3_validate_object_updates_patch():
    url = "http://127.0.0.1:8000/locations"
    newUser = {
        "id": random.randint(10000, 99999),  # Creates a location with the following attributes
        "city": "Denver PATCH",
        "country": "United States PATCH",
    }
    postObject = requests.post(url, json=newUser)  # POST operation for updating the new location
    response_body = postObject.json()  # Converts the response into JSON
    location_id = response_body["id"]  # Assigns the id to the location_id variable for later use
    updatedUser = {
        "city": "Denver AUTOMATED (PATCH)",  # Updates the location with the following attributes
        "country": "United States AUTOMATED (PATCH)",
        "id": location_id  # id must be included in the JSON payload which is why we captured it above
    }
    assert response_body["id"] == location_id
    patchObject = requests.patch(url + f'/{location_id}', json=updatedUser)  # PATCH operation for updated location info
    updated_response_body = patchObject.json()
    assert updated_response_body["id"] == location_id  # Validate id matches as expected
    assert updated_response_body["country"] == "United States AUTOMATED (PATCH)"  # Validate country was updated
    assert updated_response_body["city"] == "Denver AUTOMATED (PATCH)"  # Validate city was successfully updated
    print(updated_response_body)


# Validate PATCH request for updating a location record using /location endpoint
def test_4_validate_object_updates_put():
    url = "http://127.0.0.1:8000/locations"
    newUser = {
        "id": random.randint(10000, 99999),  # Creates a location with the following attributes
        "city": "Denver PUT",
        "country": "United States PUT",
    }
    postObject = requests.post(url, json=newUser)  # POST operation for updating the new location
    response_body = postObject.json()  # Converts the response into JSON
    location_id = response_body["id"]  # Assigns the id to the location_id variable for later use
    updatedUser = {
        "city": "Denver AUTOMATED (PUT)",  # Updates the location with the following attributes
        "country": "United States AUTOMATED (PUT)",
        "id": location_id  # id must be included in the JSON payload which is why we captured it above
    }
    patchObject = requests.put(url + f'/{location_id}', json=updatedUser)  # PATCH operation for updated location info
    updated_response_body = patchObject.json()
    assert updated_response_body["id"] == location_id  # Validate id matches as expected
    assert updated_response_body["country"] == "United States AUTOMATED (PUT)"  # Validate country was updated
    assert updated_response_body["city"] == "Denver AUTOMATED (PUT)"  # Validate city was successfully updated
    print(updated_response_body)
