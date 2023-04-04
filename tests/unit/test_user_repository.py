from pytest import raises
from pytest import fixture

from io_lottery.repositories import UserRepository


@fixture
def user_repository() -> UserRepository:
    return UserRepository()


def test_can_instantiate_user_repository(
        user_repository: UserRepository,
) -> None:
    pass


def test_raises_on_add_method(
        user_repository: UserRepository,
) -> None:
    with raises(NotImplementedError):
        user_repository.add()


def test_raises_on_put_method(
        user_repository: UserRepository,
) -> None:
    with raises(NotImplementedError):
        user_repository.put()
