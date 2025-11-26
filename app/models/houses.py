from sqlmodel import SQLModel, Field



class Dorms(SQLModel, table=True):
    dormId: int = Field(default=None, primary_key=True)
    firstName: str
    lastName: str
    Gender: str
    City: str
    DistanceFromBase: int



room1 = [[None] * 8] * 10
