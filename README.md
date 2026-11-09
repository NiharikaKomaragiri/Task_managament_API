# Task Management System

A RESTful API application built using Python, FastAPI, SQLAlchemy, and SQLite to manage tasks efficiently.

## Features

- Create new tasks.
- Retrieve all tasks.
- Retrieve a task by ID.
- Update existing tasks.
- Delete tasks.
- Set task priority (Low, Medium, High).
- Track task status (Pending, In Progress, Completed).
- Input validation using Pydantic.
- Pagination for retrieving tasks.
- Error handling for database operations.
- Automated API testing using Pytest.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Uvicorn
- HTTPX

## Project Structure

```text
Task_Management/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── test_main.py
├── requirements.txt
├── README.md
└── tasks.db
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/NiharikaKomaragiri/Task_managament_API.git>
cd Task_Management
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The application runs at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /tasks | Create a task |
| GET | /tasks | Retrieve all tasks |
| GET | /tasks/{task_id} | Retrieve a task by ID |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

### Pagination Example

```text
GET /tasks?skip=0&limit=5
```

- `skip`: Number of records to skip.
- `limit`: Maximum number of records to retrieve.

## Database

The application uses SQLite with SQLAlchemy ORM.

The task table stores:

- ID
- Title
- Description
- Status
- Priority
- Created timestamp

## Testing

Run automated tests using:

```bash
pytest -v
```

The project currently has **15 passing automated tests** covering API functionality, validation, pagination, and error scenarios.

## Learning Outcomes

- Developed REST APIs using FastAPI.
- Implemented database integration using SQLAlchemy.
- Applied request and response validation using Pydantic.
- Implemented CRUD operations.
- Practised exception handling and automated testing.
- Learned API documentation using Swagger UI.