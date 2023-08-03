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
    new_object = {
        "id": random.randint(
            10000, 99999
        ),  # Creates a new location with the following attributes
        "city": "Denver AUTOMATED (POST)",
        "country": "United States AUTOMATED (POST)",
    }
    post_object = requests.post(url, json=new_object)
    response_body = post_object.json()
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
    new_location = {
        "id": random.randint(
            10000, 99999
        ),  # Creates a location with the following attributes
        "city": "Denver PATCH",
        "country": "United States PATCH",
    }
    post_object = requests.post(
        url, json=new_location
    )  # POST operation for updating the new location
    response_body = post_object.json()  # Converts the response into JSON
    location_id = response_body[
        "id"
    ]  # Assigns the id to the location_id variable for later use
    updated_location = {
        "city": "Denver AUTOMATED (PATCH)",  # Updates the location with the following attributes
        "country": "United States AUTOMATED (PATCH)",
        "id": location_id,  # id must be included in the JSON payload which is why we captured it above
    }
    assert response_body["id"] == location_id
    patch_object = requests.patch(
        url + f"/{location_id}", json=updated_location
    )  # PATCH operation for updated location info
    updated_response_body = patch_object.json()
    assert updated_response_body["id"] == location_id  # Validate id matches as expected
    assert (
            updated_response_body["country"] == "United States AUTOMATED (PATCH)"
    )  # Validate country was updated
    assert (
            updated_response_body["city"] == "Denver AUTOMATED (PATCH)"
    )  # Validate city was successfully updated
    print(updated_response_body)


# Validate PATCH request for updating a location record using /location endpoint
def test_4_validate_object_updates_put():
    url = "http://127.0.0.1:8000/locations"
    new_location = {
        "id": random.randint(
            10000, 99999
        ),  # Creates a location with the following attributes
        "city": "Denver PUT",
        "country": "United States PUT",
    }
    post_object = requests.post(
        url, json=new_location
    )  # POST operation for updating the new location
    response_body = post_object.json()  # Converts the response into JSON
    location_id = response_body[
        "id"
    ]  # Assigns the id to the location_id variable for later use
    updated_user = {
        "city": "Denver AUTOMATED (PUT)",  # Updates the location with the following attributes
        "country": "United States AUTOMATED (PUT)",
        "id": location_id,  # id must be included in the JSON payload which is why we captured it above
    }
    patch_object = requests.put(
        url + f"/{location_id}", json=updated_user
    )  # PATCH operation for updated location info
    updated_response_body = patch_object.json()
    assert updated_response_body["id"] == location_id  # Validate id matches as expected
    assert (
            updated_response_body["country"] == "United States AUTOMATED (PUT)"
    )  # Validate country was updated
    assert (
            updated_response_body["city"] == "Denver AUTOMATED (PUT)"
    )  # Validate city was successfully updated
    print(updated_response_body)


# Validate DELETE request for deleting a location record using /location endpoint
def test_5_validate_location_object_delete():
    url = "http://127.0.0.1:8000/locations"
    new_location = {
        "id": random.randint(
            10000, 99999
        ),  # Creates a location with the following attributes
        "city": "Denver DELETE",
        "country": "United States DELETE",
    }
    post_object = requests.post(
        url, json=new_location
    )  # POST operation for updating the new location
    response_body = post_object.json()  # Converts the response into JSON
    location_id = response_body[
        "id"
    ]  # Assigns the id to the location_id variable for later use
    delete_object = requests.delete(
        url + f"/{location_id}"
    )  # DELETE operation for test location
    updated_response_body = delete_object.json()
    assert delete_object.status_code == 200
    assert updated_response_body["message"] == "Location has been successfully deleted."
    get_deleted_object = requests.get(url + f"{location_id}")
    assert get_deleted_object.status_code == 404
    print(updated_response_body)
