from sqlmodel import create_engine, Session
from app.models.dorms import Dorms
from app.dal.soldiers_dal import most_far_soldier


engine = create_engine("sqlite:///database.db")

def assignment_to_dorms():
    dorms = range(1,3) # you can easily add another dorm
    rooms =  range(1,11)
    soldiers_per_room = range(1,9)
    for dorm in dorms:
        for room in rooms:
            for _ in soldiers_per_room:
                soldier = most_far_soldier()
                assignment = Dorms(
                    Dorm = dorm,
                    Room = room,
                    soldeirId = soldier,
                )

                with Session(engine) as session:
                    session.add(assignment)
                    session.commit()
                    session.refresh(assignment)

