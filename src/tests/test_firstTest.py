import requests
import json


def test_get_responds_200():
    response = requests.get("http://api.zippopotam.us/us/80602")
    response_body = response.json()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response_body["places"][0]["place name"] == "Brighton"
