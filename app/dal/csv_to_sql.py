from sqlmodel import SQLModel, Field, create_engine, Session, select
from fastapi import FastAPI, UploadFile
import csv
import uvicorn
import io
from app.services.dorms_sevices import assignment_to_dorms
from app.services.soldier_services import add_soldier
from app.models.dorms import Dorms

app = FastAPI()
items = []

engine = create_engine("sqlite:///database.db")


@app.post("/assignWithCsv")
def upload_csv(file: UploadFile):
    # checking that the file is csv file
    if file.content_type != "text/csv":
        return {"invalid file": "file must be a csv"}

    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    next(reader)
    rows = list(reader)
    for line in rows:  # create and add soldier object from csv line
        add_soldier(line)
    # SQLModel.metadata.create_all(engine)
    assignment_to_dorms() # auto assign soldiers based on distance

    return rows

SQLModel.metadata.create_all(engine)






if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8010)
