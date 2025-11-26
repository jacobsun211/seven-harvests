from sqlmodel import SQLModel, Field
from typing import Optional


class Soldiers(SQLModel, table=True):
    soldierId: int = Field(default=None, primary_key=True)
    firstName: str
    lastName: str
    Gender: str
    City: str
    DistanceFromBase: int
    assignmentStatus: Optional[bool]
    assignedTo: Optional[int]