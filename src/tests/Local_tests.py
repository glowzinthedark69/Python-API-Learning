import requests
import json
import random


# Validate GET request for all users using /users endpoint
def test_1_validate_objects_returned():
    response = requests.get("http://127.0.0.1:5000/users")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response_body, list)
    print(response_body)


# Validate POST request for new user creation using /users endpoint
def test_2_validate_object_creation():
    url = "http://127.0.0.1:5000/users"
    newObject = {
        "userId": random.randint(1000, 9999),
        "name": "John Tester",
        "city": "Denver",
        "country": "United States",
        "jobTitle": "Software Test Engineer III"
    }
    postObject = requests.post(url, json=newObject)
    response_body = postObject.json()
    print(response_body)
    new_user_id = response_body["userId"]
    print(new_user_id)
    assert response_body["userId"] == new_user_id
    assert response_body["name"] == "John Tester"
    assert response_body["jobTitle"] == "Software Test Engineer III"
    print(response_body)


# Validate PATCH request for updating a user record using /users endpoint
def test_3_validate_object_updates():
    url = "http://127.0.0.1:5000/users"
    newUser = {
        "userId": random.randint(1000, 9999),  # Creates a new user with the following attributes
        "name": "John Tester",
        "city": "Denver",
        "country": "United States",
        "jobTitle": "Software Test Engineer III"
    }
    postObject = requests.post(url, json=newUser)  # POST operation for creating the new user
    response_body = postObject.json()  # Converts the response into JSON
    new_user_id = response_body["userId"]  # Assigns the userId to the new_user_id variable for later use
    updatedUser = {
        "name": "John Tester UPDATED",  # Updates the user with the following attributes
        "city": "Seattle",
        "userId": new_user_id  # userId must be included in the JSON payload which is why we captured it above
    }
    patchObject = requests.patch(url + f'/{new_user_id}', json=updatedUser)  # PATCH operation for the updated user info
    updated_response_body = patchObject.json()
    assert updated_response_body["userId"] == new_user_id
    assert updated_response_body["name"] == "John Tester UPDATED"  # Validate that the name was successfully updated
    assert updated_response_body["city"] == "Seattle"  # Validate that the city was successfully updated
    print(updated_response_body)
