from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def root() -> dict:
    return {'data': {'name': 'jahghee'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from db.'}
    else:
        return {'data':f'{limit} blogs from db.'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'create blog with title as {request.title}'}