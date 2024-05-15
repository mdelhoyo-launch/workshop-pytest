import requests


def test_get():
    url = "http://127.0.0.1:8000/studios"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_post():
    url = "http://127.0.0.1:8000/studios/post"
    new_studio = {
        "studio_name": "Another cool Studio"
    }
    response = requests.post(url, json=new_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data["studio_name_created"] == "Another cool Studio"


def test_put():
    url = "http://127.0.0.1:8000/disciplines/put"
    update_studio = {
        "discipline_name": "My cool Discipline",
        "studio_name": "Software Engineering"
    }
    response = requests.put(url, json=update_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_delete():
    url = "http://127.0.0.1:8000/studios/delete"
    delete_studio = {
        "studio_name": "Another cool Studio"
    }
    response = requests.delete(url, json=delete_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
