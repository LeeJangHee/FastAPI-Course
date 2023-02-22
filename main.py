from fastapi import FastAPI

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
