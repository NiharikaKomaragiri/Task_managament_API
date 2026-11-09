from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from typing import Optional, Literal
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)

    status: Literal["Pending", "In Progress", "Completed"] = "Pending"

    priority: Literal["Low", "Medium", "High"] = "Medium"
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot contain only spaces")
        return value.strip()


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[Literal["Pending", "In Progress", "Completed"]] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Title cannot contain only spaces")
        return value.strip() if value is not None else value

    @model_validator(mode="after")
    def validate_at_least_one_field(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")
        return self
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)