from sqlmodel import SQLModel, Field, create_engine, Session, select,update,func
from app.models.soldiers import Soldiers

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


def most_far_soldier():
    with Session(engine) as session:
        statement = select(Soldiers).where(Soldiers.assignmentStatus == False ).order_by(Soldiers.DistanceFromBase)
        soldier = session.exec(statement).all()
        update_assignmentStatus_soldier(soldier[0])
        return soldier


def update_assignmentStatus_soldier(soldier):
    with Session(engine) as session:
        statement = select(Soldiers).where(Soldiers.soldierId == soldier.soldierId)
        result = session.exec(statement)
        soldier = result.one()
        soldier.assignmentStatus = True
        session.add(soldier)
        session.commit()
        session.refresh(soldier)
        print(soldier)
        return soldier


def all_soldiers_assigned():
    with Session(engine) as session:
        statement = select (func.count(Soldiers)).where(Soldiers.assignmentStatus == True)
        result = session.exec(statement).all()
        return result





