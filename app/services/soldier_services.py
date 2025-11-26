from sqlmodel import SQLModel, Field, create_engine, Session, select
from app.models.soldiers import Soldiers

engine = create_engine("sqlite:///database.db")


def add_soldier(soldier):
    soldier = Soldiers(
        soldierId = soldier[0],
        firstName = soldier[1],
        lastName = soldier[2],
        Gender = soldier[3],
        City = soldier[4],
        DistanceFromBase = soldier[5],
        assignmentStatus = False,
        assignedTo = None,
    )
    with Session(engine) as session:
        session.add(soldier)
        session.commit()
        session.refresh(soldier)
    print(f"soldier created: {soldier}")

