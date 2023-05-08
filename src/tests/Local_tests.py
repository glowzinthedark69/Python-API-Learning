import requests
import json
import random
import names


def test_1_validate_object1_contents_GET():
    response = requests.get("http://127.0.0.1:5000/users")
    response_body = response.json()
    print(response_body)
    user = response_body[0]  # get the first user in the list
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert user["userId"] == 1234
    assert user["name"] == "John Smithson"
    assert user["jobTitle"] == "Software Test Engineer I"
    assert user["city"] == "Seattle"
    print(user)


def test_2_validate_objects_returned_GetAll():
    response = requests.get("http://127.0.0.1:5000/users")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    print(response_body)


def test_3_validate_object_creation_POST():
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


def test_4_validate_object_contents_GET():
    response = requests.get("http://127.0.0.1:5000/users")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert isinstance(response_body, list)
    print(response_body)
