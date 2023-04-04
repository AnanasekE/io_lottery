from unittest.mock import Mock

from pytest import fixture

from io_lottery.controllers import AddUserController, AddUserRequest
from io_lottery.repositories import UserRepository
from tests.integration.test_users import UserPayloadFactory


@fixture
def user_repository() -> Mock:
    return Mock(UserRepository)


@fixture
def add_user_controller(user_repository: Mock) -> AddUserController:
    return AddUserController(repository=user_repository)


def test_can_instantiate_add_user_controller(
        capsys,
        add_user_controller: AddUserController,
) -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    add_user_controller.add(request=request)
    actual = capsys.readouterr().out
    expected = f"{payload}\n"
    assert actual == expected


def test_calls_repository_on_add_method(
        add_user_controller: AddUserController,
        user_repository: Mock,
) -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    add_user_controller.add(request)
    assert user_repository.add.call_count > 0


def test_add_user_request_has_json_field() -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    assert request.json


