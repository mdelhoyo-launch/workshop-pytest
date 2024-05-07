import requests


def test_create_new_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.json())

    assert response.status_code == 201


def test_create_new_user_fail():
    url = "https://reqres.in/api/users"
    data = {
        "nae": "Paulo Oliveira",
        "moies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.json())

    assert response.status_code == 201
