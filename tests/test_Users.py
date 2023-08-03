import pytest
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


def test_5_validate_user_object_delete():
    url = "http://127.0.0.1:8000/users"
    # POST operation for updating the new location
    new_user = {
        "userId": random.randint(
            10000, 99999
        ),  # Creates a new user with the following attributes
        "name": "John DELETE",
        "city": "Denver DELETE",
        "country": "United States DELETE",
        "jobTitle": "DELETED",
    }
    # Converts the response into JSON
    post_object = requests.post(
        url, json=new_user
    )
    # Assigns the id to the user_id variable for later use
    response_body = post_object.json()
    user_id = response_body[
        "userId"
    ]
    # Request to delete the test user with the user id captured above
    delete_object = requests.delete(
        url + f"/{user_id}"
    )
    # Assertions to verify that the DELETE was successful
    updated_response_body = delete_object.json()
    assert delete_object.status_code == 200
    assert updated_response_body["message"] == "User has been successfully deleted."
    print(updated_response_body)
    get_deleted_object = requests.get(url + f"{user_id}")
    assert get_deleted_object.status_code == 404
    deleted_response_body = get_deleted_object.json()
    expected_response = {
        "detail": "Not Found"
    }
    assert deleted_response_body == expected_response
    print(deleted_response_body)


def test_sample_items():
    try:
        response = requests.get("http://127.0.0.1:8000/users")
        response.raise_for_status()  # Raise exception if the request failed
    except requests.RequestException as e:
        pytest.fail(f"Request failed: {e}")

    try:
        response_body = response.json()
    except ValueError:
        pytest.fail("Failed to parse response as JSON")

    # Randomly sample 250 items from the response body, or all items if there are less than 250
    sample_size = min(250, len(response_body))
    sample = random.sample(response_body, sample_size)

    for item in sample:
        # Assert that the item is a dictionary
        assert isinstance(item, dict)

        # Assert that the item has an 'id' key
        assert 'userId' in item

        # Assert that the id is not None
        assert item['userId'] is not None

        # Assert that the id is a number
        assert isinstance(item['userId'], int) or isinstance(item['userId'], float)

        # Assert that the id is above -1 and not equal to 0
        assert item['userId'] > -1
        assert item['userId'] != 0

        # Assert that the item has a 'city' key
        assert 'city' in item

        # Assert that the city is not None
        assert item['city'] is not None

        # Assert that the city is a string
        assert isinstance(item['city'], str)

        # Assert that the item has a 'country' key
        assert 'country' in item

        # Assert that the country is not None
        assert item['country'] is not None

        # Assert that the country is a string
        assert isinstance(item['country'], str)

        # Assert that the item has a 'job title' key
        assert 'jobTitle' in item

        # Assert that the country is not None
        assert item['jobTitle'] is not None

        # Assert that the country is a string
        assert isinstance(item['jobTitle'], str)
