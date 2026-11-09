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