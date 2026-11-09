from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal, Base




# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI
app = FastAPI(
    title="Task Management System",
    description="A REST API application to manage tasks",
    version="1.0.0"
)


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, gt=0, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db, skip, limit)

# Home endpoint
@app.get("/")
def home():

    return {
        "message": "Welcome to Task Management System"
    }


# CREATE: Create a new task
@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):

    return crud.create_task(db, task)


# READ: Retrieve all tasks
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    return crud.get_tasks(db, skip, limit)


# READ: Retrieve task by ID
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):

    db_task = crud.get_task(db, task_id)

    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return db_task


# UPDATE: Update task
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_existing_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):

    updated_task = crud.update_task(db, task_id, task)

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task


# DELETE: Delete task
@app.delete("/tasks/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):

    deleted_task = crud.delete_task(db, task_id)

    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }
    