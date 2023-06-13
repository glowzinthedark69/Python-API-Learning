import requests
import json
import random


# Validate GET request for all users using /users endpoint
def test_1_validate_objects_returned():
    response = requests.get("http://127.0.0.1:8000/locations")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response_body, list)
    print(response_body)


# Validate POST request for new user creation using /users endpoint
def test_2_validate_object_creation():
    url = "http://127.0.0.1:8000/locations"
    newObject = {
        "id": random.randint(10000, 99999),     # Creates a new user with the following attributes
        "city": "Denver AUTOMATED",
        "country": "United States AUTOMATED",
    }
    postObject = requests.post(url, json=newObject)
    response_body = postObject.json()
    print(response_body)
    new_location_id = response_body["id"]
    print(new_location_id)
    assert response_body["id"] == new_location_id
    assert response_body["city"] == "Denver AUTOMATED"
    assert response_body["country"] == "United States AUTOMATED"
    print(response_body)


# Validate PATCH request for updating a user record using /users endpoint
def test_3_validate_object_updates():
    url = "http://127.0.0.1:8000/locations"
    newUser = {
        "id": random.randint(10000, 99999),  # Creates a user with the following attributes
        "city": "Denver PATCH",
        "country": "United States PATCH",
    }
    postObject = requests.post(url, json=newUser)  # POST operation for updating the new user
    response_body = postObject.json()  # Converts the response into JSON
    location_id = response_body["id"]  # Assigns the userId to the new_user_id variable for later use
    updatedUser = {
        "city": "Denver AUTOMATED (PATCH)",  # Updates the user with the following attributes
        "country": "United States AUTOMATED (PATCH)",
        "id": location_id  # userId must be included in the JSON payload which is why we captured it above
    }
    patchObject = requests.patch(url + f'/{location_id}', json=updatedUser)  # PATCH operation for updated user info
    updated_response_body = patchObject.json()
    assert updated_response_body["id"] == location_id   # Validate id matches as expected
    assert updated_response_body["country"] == "United States AUTOMATED (PATCH)"  # Validate country was updated
    assert updated_response_body["city"] == "Denver AUTOMATED (PATCH)"  # Validate city was successfully updated
    print(updated_response_body)
