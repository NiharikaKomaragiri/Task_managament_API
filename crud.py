from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

import models
import schemas


# CREATE: Add a new task
def create_task(db: Session, task: schemas.TaskCreate):
    try:
        db_task = models.Task(**task.model_dump())

        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    except SQLAlchemyError:
        db.rollback()
        raise


# READ: Retrieve all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Task).offset(skip).limit(limit).all()


# READ: Retrieve a task by ID
def get_task(db: Session, task_id: int):

    return db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()


# UPDATE: Update an existing task
def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    try:
        db_task = get_task(db, task_id)

        if db_task is None:
            return None

        update_data = task.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_task, key, value)

        db.commit()
        db.refresh(db_task)

        return db_task

    except SQLAlchemyError:
        db.rollback()
        raise


# DELETE: Delete an existing task
def delete_task(db: Session, task_id: int):
    try:
        db_task = get_task(db, task_id)

        if db_task is None:
            return None

        db.delete(db_task)
        db.commit()

        return db_task

    except SQLAlchemyError:
        db.rollback()
        raise