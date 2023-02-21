import requests
import json


def test_1():
    response = requests.get("http://api.zippopotam.us/us/80602")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["places"][0]["place name"] == "Brighton"
    assert len(response_body["places"]) == 1


def test_2():
    response = requests.get("https://api.restful-api.dev/objects")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    print(response_body)


def test_3():
    url = "https://api.restful-api.dev/objects"
    newObject = {
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2027,
            "price": 18499.99,
            "CPU model": "Intel Core i99",
            "Hard disk size": "100 TB",
            "created by": "mkrahl1"
        }
    }
    postObject = requests.post(url, json=newObject)
    responseBody = postObject.json()
    print(responseBody)


def test_4():
    response = requests.get("https://api.restful-api.dev/objects?id=ff808181866731b50186700f9678017d")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    print(response_body)
