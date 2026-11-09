from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Task Management System"
    }


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Pytest Practice",
            "description": "Testing CRUD operations",
            "status": "Pending",
            "priority": "High"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Pytest Practice"


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_priority():
    response = client.post(
        "/tasks",
        json={
            "title": "Invalid Task",
            "description": "Testing validation",
            "status": "Pending",
            "priority": "Urgent"
        }
    )

    assert response.status_code == 422
    
def test_update_task():
    # First create a task
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old Title",
            "description": "Old Description",
            "status": "Pending",
            "priority": "Low"
        }
    )

    task_id = create_response.json()["id"]

    # Update the task
    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Title",
            "priority": "High"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["priority"] == "High"
    
def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete Me",
            "description": "Testing delete",
            "status": "Pending",
            "priority": "Medium"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
    
def test_task_not_found():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
    
def test_update_nonexistent_task():
    response = client.put(
        "/tasks/999999",
        json={
            "title": "Updated Task"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
    
def test_whitespace_title():
    response = client.post(
        "/tasks",
        json={
            "title": "     ",
            "description": "Testing empty title",
            "status": "Pending",
            "priority": "High"
        }
    )

    assert response.status_code == 422
    
def test_pagination_valid():
    response = client.get("/tasks?skip=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5


def test_pagination_invalid_skip():
    response = client.get("/tasks?skip=-1&limit=5")
    assert response.status_code == 422


def test_pagination_invalid_limit():
    response = client.get("/tasks?skip=0&limit=0")
    assert response.status_code == 422


def test_pagination_limit_max():
    response = client.get("/tasks?skip=0&limit=101")
    assert response.status_code == 422
    
def test_empty_update():
    response = client.put("/tasks/1", json={})
    assert response.status_code == 422


def test_whitespace_update_title():
    response = client.put("/tasks/1", json={"title": "   "})
    assert response.status_code == 422