from sqlmodel import SQLModel, Field, create_engine, Session, select



engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)