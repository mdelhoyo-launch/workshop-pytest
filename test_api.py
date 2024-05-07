import requests


def test_get_postman_echo():
    url = "https://postman-echo.com/get"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_post_postman_echo():
    url = "https://postman-echo.com/post?foo1=bar1&foo2=bar2"
    response = requests.post(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_patch_postman_echo():
    url = "https://postman-echo.com/patch?foo1=bar1&foo2=bar2"
    response = requests.patch(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_delete_postman_echo():
    url = "https://postman-echo.com/delete?foo1=bar1&foo2=bar2"
    response = requests.delete(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
