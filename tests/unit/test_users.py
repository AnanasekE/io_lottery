from factory import DictFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat

from io_lottery.app import add_user, get_user, app, upgrade_user, put_user


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_returns_sent_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='POST', json=payload):
        actual = add_user()
    assert actual.json == payload


def test_returns_unimplemented() -> None:
    actual = get_user()
    assert actual.status_code == 501


def test_returns_unimplemented_on_put_user() -> None:
    actual = put_user(24)
    assert actual.status_code == 200

def test_returns_unimplemented_on_delete_user() -> None:
    actual = delete_user(24)
    assert actual.status_code == 200

def test_returns_unimplemented_on_patch_user() -> None:
    actual = patch_user(24)
    assert actual.status_code == 200

def test_upgrade_user() -> None:
    actual = upgrade_user(24)
    assert actual.status_code == 501
