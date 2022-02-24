from urllib import response
from fastapi.testclient import TestClient
from main import app

'''
test_index():
test_readItem:
test_createItem:
'''
client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" :  "hello world"}

def test_readItem():
    response = client.get("/items/foo"  , params={"item_id" : "1"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }
def test_createItem():
    response = client.post(
        "/items/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }