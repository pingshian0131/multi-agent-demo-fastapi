from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_get_item_endpoint():
    response = client.get("/items/123")
    assert response.status_code == 200
    assert response.json() == {"item_id": 123}

def test_add_endpoint():
    response = client.post("/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_update_item_endpoint():
    response = client.put("/item/123", json={"title": "test"})
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Item 123 updated"}

def test_delete_item_endpoint():
    response = client.delete("/item/123")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Item 123 deleted"}