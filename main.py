#  import
from typing import Union
from fastapi import FastAPI

# instance 
app = FastAPI()

#decorate
@app.get("/")
def read_root():
    return {"data": [{"name": "sarth", "age": 45}]}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
