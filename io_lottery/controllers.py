from dataclasses import dataclass

from io_lottery.repositories import UserRepository


@dataclass
class AddUserRequest:
    json: dict


@dataclass
class PutUserRequest:
    json: dict


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add()
        print(request.json)


class PutUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def put(self, request: PutUserRequest, id: int) -> None:
        self._repository.put()
        print(request.json, id)


class PatchUserController:
    def patch(self, id: int):
        raise NotImplementedError


class DeleteUserController:
    def delete(self, id: int):
        raise NotImplementedError
