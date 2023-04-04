from factory import DictFactory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyFloat

from io_lottery.app import app


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count: object = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_can_add_user_on_post() -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        result = c.post("/users", json=payload)
        assert result.status_code == 200


def test_prints_added_user_on_post(capsys) -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        c.post("/users", json=payload)
    actual = capsys.readouterr().out
    sorted_dict = {k: payload[k] for k in sorted(payload)}
    expected = f"{sorted_dict}\n"
    assert actual == expected


def test_prints_put_user_on_put(capsys) -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        c.put("/users/24", json=payload)
    actual = capsys.readouterr().out
    sorted_dict = {k: payload[k] for k in sorted(payload)}
    expected = f"{sorted_dict}\n"
    assert actual == expected


def test_prints_patch_user_on_patch(capsys) -> None:
    pass  # nie mam pomysłu jak sprawdzić dla jednego klucza


def test_returns_unimplemented() -> None:
    with app.test_client() as c:
        actual = c.get("/users/24")
    assert actual.status_code == 501


def test_returns_unimplemented_on_new_user() -> None:
    with app.test_client() as c:
        actual = c.post("/users_new")
    assert actual.status_code == 500


def test_returns_unimplemented_on_patch_user() -> None:
    with app.test_client() as c:
        actual = c.patch("/users/24")
    assert actual.status_code == 501


def test_returns_unimplemented_on_delete_user() -> None:
    with app.test_client() as c:
        actual = c.delete("/users/24")
    assert actual.status_code == 204


def test_user_upgrade() -> None:
    with app.test_client() as c:
        actual = c.put("/users/24")
    assert actual.status_code == 200
