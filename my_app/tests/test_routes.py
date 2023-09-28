def test_hello_world(client):
    response = client.get("/hello_world/hello_world")
    assert response.status_code == 200
    assert response.json == {"hello": "world"}


def test_hello_all_worlds(client):
    response = client.get("/hello_world/hello_all_worlds")
    assert response.status_code == 200
    assert response.json == [
        {"world_id": "home", "name": "Earth"},
    ]


def test_get_world(client):
    response = client.get("/hello_world/home")
    assert response.status_code == 200
    assert response.json == {
        "world_id": "home",
        "name": "Earth",
    }


def test_swagger_ui(client):
    response = client.get("/swagger.json")
    assert response.status_code == 200
    assert b'"swagger": "2.0"' in response.data
