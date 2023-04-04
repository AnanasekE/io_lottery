import pytest
from _pytest.python_api import RaisesContext
from flask import Flask, Response, request, jsonify

from io_lottery.controllers import AddUserController, AddUserRequest, GetUserController, PutUserController, \
    PatchUserController, DeleteUserController, PutUserRequest
from io_lottery.repositories import UserRepository
from io_lottery.views import UserView

app = Flask(__name__)


@app.get("/users/<id>")
def get_user(id: int) -> Response:
    controller = GetUserController()
    try:
        controller.get(id)
    except NotImplementedError:
        pass
    return Response(status=501)


@app.post("/users")
def add_user() -> Response:
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    controller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json)


@app.put("/users/<id>")
def put_user(id: int) -> Response:
    repository = UserRepository()
    controller = PutUserController(repository=repository)
    controller.put(request=PutUserRequest(json=request.json), id=id)
    return Response(status=200)


@app.patch("/users/<id>") # nie mam pomysłu jak to zrobić, aby return był jednego klucza
def patch_user(id: int) -> Response:
    controller = PatchUserController()
    try:
        controller.patch(id)
    except NotImplementedError:
        pass
    return Response(status=200)


@app.delete("/users/<id>")
def delete_user(id: int) -> Response:
    controller = DeleteUserController()
    try:
        controller.delete(id)
    except NotImplementedError:
        pass
    return Response(status=204)

# @app.put("/users/<id>")
# def upgrade_user(id: int) -> Response:
#     return Response(status=501)


app.add_url_rule("/users_new", view_func=UserView.as_view("users_new"))
