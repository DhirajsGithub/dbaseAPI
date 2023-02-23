from typing import Union
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import baseConverter

app = FastAPI()


# convert button clicked --> get request
@app.get("/")
def index():
    return {"Make a post requiest @ "/" ": "ans"}


class Data(BaseModel):
    number: str
    base: int
    convertTo: int

# override the temp.txt file with number base and convertTo


fileName = "temp.txt"


@app.post("/")
def index(request: Data):
    number = request.number
    base = int(request.base)
    convertTo = int(request.convertTo)
    return baseConverter.main(number, base, convertTo)
