from sqlmodel import SQLModel, Field
from typing import Optional


class Soldiers(SQLModel, table=True):
    soldierId: Optional[int] = Field(default=None, primary_key=True)
    firstName: Optional[str]
    lastName: Optional[str]
    Gender: Optional[str]
    City: Optional[str]
    DistanceFromBase: Optional[int]