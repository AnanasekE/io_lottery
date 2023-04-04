from unittest.mock import Mock

from pytest import fixture

from io_lottery.controllers import PutUserController, PutUserRequest
from io_lottery.repositories import UserRepository
from tests.integration.test_users import UserPayloadFactory


@fixture
def user_repository() -> Mock:
    return Mock(UserRepository)


@fixture
def add_user_controller(user_repository: Mock) -> PutUserController:
    return PutUserController(repository=user_repository)


def test_can_instantiate_put_user_controller(
        capsys,
        put_user_controller: PutUserController
) -> None:
    payload = UserPayloadFactory()
    request = PutUserRequest(json=payload)
    put_user_controller.put(request=request, id=21)
    actual = capsys.readouterr().out
    expected = f"{payload} 21\n"
    assert actual == expected


def test_calls_repository_on_put_method(
        put_user_controller: PutUserController,
        user_repository: Mock,
) -> None:
    payload = UserPayloadFactory()
    request = PutUserRequest(json=payload)
    put_user_controller.put(request, id=21)
    assert user_repository.put.call_count > 0


def test_put_user_request_has_json_field() -> None:
    payload = UserPayloadFactory()
    request = PutUserRequest(json=payload)
    assert request.json


