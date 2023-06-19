import requests
import json


def test_1_validate_object1_contents_GET():
    response = requests.get("https://api.restful-api.dev/objects/1")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["id"] == "1"
    assert response_body["name"] == "Google Pixel 6 Pro"
    assert response_body["data"]["color"] == "Cloudy White"
    assert response_body["data"]["capacity"] == "128 GB"
    print(response_body)


def test_2_validate_objects_returned_GetAll():
    response = requests.get("https://api.restful-api.dev/objects")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    print(response_body)


def test_3_validate_object_creation_POST():
    url = "https://api.restful-api.dev/objects"
    newObject = {
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2027,
            "price": 18499.99,
            "CPU model": "Intel Core i99",
            "Hard disk size": "100 TB",
            "created by": "mkrahl",
        },
    }
    postObject = requests.post(url, json=newObject)
    response_body = postObject.json()
    object_id = response_body["id"]
    print(object_id)
    assert response_body["id"] == object_id
    assert response_body["name"] == "Apple MacBook Pro 160"
    assert response_body["data"]["price"] == 18499.99
    print(response_body)


def test_4_validate_object_contents_GET():
    response = requests.get(
        "https://api.restful-api.dev/objects?id=ff80818187dae5600187ddb9978f0150"
    )
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    print(response_body)
