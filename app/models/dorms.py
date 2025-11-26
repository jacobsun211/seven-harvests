from sqlmodel import SQLModel, Field
from typing import Optional


class Dorms(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Dorm: int
    Room: int
    soldierId: Optional[int] = Field(foreign_key='soldiers.soldierId')





