#  import
from typing import Union
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


# instance
app = FastAPI()

# decorate


@app.get("/")
def index():
    return {"data": [{"name": "sarth", "age": 45}]}

# get is the operation "/" is a patth or say it as base path
# index is a path operation function
# the overall decorator is called path operation decorator

# NOTE: fast api read the file line by line

# why is the route above /blog/{id}, this is beacause /blog/{id} takes integer after /blog/
# but we will be providing string for unpublished blog hence it is better above it


@app.get("/blog/unpublished")
def unpublish():
    return {"data": "unpublished blogs"}

# dynamic routing


@app.get("/blog/{id}")
def show(id: int):
    # since from the browser we wil get string as the default one
    # fetch blog with id == id
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    # fetch comments of blog with id == id
    return {"comments": [{"comment1": "fdsjfklds"}, {"comment2": "fkdjsfk"}]}


# query parameters
@app.get("/blogs")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # defining default values to limit and published as if /blogs?limit=12&published=true not defined in url then it will show error
    # what if we don't want to define a default paramter and it's type then we can use as Optional type str and value to be nonoe
    if published:
        return {"data": f'{limit} published blogs from data base'}
    return {"data": f"{limit} blogs from data base"}

# NOTE : fastapi is smart enough to identify which is path parameter and which is query parameter
# if something is degine in funtion parameter as well in path with curly brac then it's pathe parameter


# post request

# creating a modal /schema
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    with open("temp.txt", 'w') as f:
        f.write(f"{request.title}")
        f.write(f"\n{request.body}")
        f.write(f"\n{request.published}")
    print(type(request))
    return {"data": f"blog is created with title {request.title} "}
