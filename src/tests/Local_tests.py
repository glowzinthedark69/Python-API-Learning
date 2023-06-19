import requests
import json
import random


# Validate GET request for all users using /users endpoint
def test_1_validate_objects_returned():
    response = requests.get("http://127.0.0.1:8000/users")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response_body, list)
    print(response_body)


# Validate POST request for new user creation using /users endpoint
def test_2_validate_object_creation():
    url = "http://127.0.0.1:8000/users"
    new_object = {
        "userId": random.randint(10000, 99999),
        "name": "John Tester",
        "city": "Denver",
        "country": "United States",
        "jobTitle": "Software Test Engineer III",
    }
    post_object = requests.post(url, json=new_object)
    response_body = post_object.json()
    print(response_body)
    new_user_id = response_body["userId"]
    print(new_user_id)
    assert response_body["userId"] == new_user_id
    assert response_body["name"] == "John Tester"
    assert response_body["jobTitle"] == "Software Test Engineer III"
    print(response_body)


# Validate PATCH request for updating a user record using /users endpoint
def test_3_validate_object_updates():
    url = "http://127.0.0.1:8000/users"
    new_user = {
        "userId": random.randint(
            10000, 99999
        ),  # Creates a new user with the following attributes
        "name": "John Tester",
        "city": "Denver",
        "country": "United States",
        "jobTitle": "Software Test Engineer III",
    }
    post_object = requests.post(
        url, json=new_user
    )  # POST operation for creating the new user
    response_body = post_object.json()  # Converts the response into JSON
    user_id = response_body[
        "userId"
    ]  # Assigns the userId to the new_user_id variable for later use
    updated_user = {
        "name": "John Tester UPDATED",  # Updates the user with the following attributes
        "city": "Seattle",
        "userId": user_id,  # userId must be included in the JSON payload which is why we captured it above
    }
    patch_object = requests.patch(
        url + f"/{user_id}", json=updated_user
    )  # PATCH operation for the updated user info
    updated_response_body = patch_object.json()
    assert updated_response_body["userId"] == user_id
    assert (
        updated_response_body["name"] == "John Tester UPDATED"
    )  # Validate that the name was successfully updated
    assert (
        updated_response_body["city"] == "Seattle"
    )  # Validate that the city was successfully updated
    print(updated_response_body)
