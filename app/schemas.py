from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class issue_status(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class issue_priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class issue_create(BaseModel):
   title: str = Field(min_length=3, max_length=100)
   description: str = Field(min_length=10, max_length=1000)
   priority: issue_priority = issue_priority.medium 

class issue_update(BaseModel):
   title: Optional[str] = Field(default=None, min_length=3, max_length=100)
   description: Optional[str] = Field(default=None, min_length=10, max_length=1000)
   priority: Optional[issue_priority] = None
   status: Optional[issue_status] = None

class issue_out(BaseModel):
   id: str
   title: str
   description: str
   priority: issue_priority
   status: issue_status
