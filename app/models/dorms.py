from sqlmodel import SQLModel, Field
from typing import Optional


class Dorms(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    Dorm: int
    Room: int
    soldierId: Optional[int] = Field(foreign_key='soldiers.soldierId')





# dorm = 1
# rooms = range(1,8)
# soldier = "id"
# row = []
# for roomNum in rooms:
#     row.append([dorm,roomNum,soldier])


# print(row)
# room1 = [[None] * 8] * 10
