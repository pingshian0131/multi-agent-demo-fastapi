import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_empty_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo():
    response = client.post("/todos", json={"task": "Test task"})
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["task"] == "Test task"


def test_get_todos_after_create():
    # First create a todo
    client.post("/todos", json={"task": "Another test task"})
    
    # Then get all todos
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0
    assert any(todo["task"] == "Another test task" for todo in todos)


def test_delete_todo():
    # First create a todo
    create_response = client.post("/todos", json={"task": "Task to delete"})
    todo_id = create_response.json()["id"]
    
    # Then delete it
    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["status"] == "success"
    assert f"To-Do item with id {todo_id} deleted" in delete_response.json()["message"]
    
    # Verify it's gone
    get_response = client.get("/todos")
    assert not any(todo["id"] == todo_id for todo in get_response.json())


def test_delete_nonexistent_todo():
    # Try to delete a todo with an ID that doesn't exist
    response = client.delete("/todos/9999")
    assert response.status_code == 200  # Note: Could be 404 depending on your implementation
    assert response.json()["status"] == "error"
    assert "not found" in response.json()["message"]
