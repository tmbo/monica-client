import uuid

import pytest


@pytest.fixture
def random_name():
    return uuid.uuid4().hex


def gender_id_by_type(typ, monica_client):
    gs = monica_client.genders()

    for g in gs:
        if g.get("type") == typ:
            return g.get("id")
    return None


@pytest.fixture
def default_gender(monica_client):
    return gender_id_by_type("O", monica_client)


def test_create_contact(monica_client, random_name, default_gender):
    c = monica_client.create_contact(random_name, default_gender)

    assert c is not None
    assert c.get("first_name") == random_name


def test_get_me(monica_client):
    me = monica_client.me()

    assert me.get("object") == "user"


def test_find_contact(monica_client, random_name, default_gender):
    c = monica_client.create_contact(random_name, default_gender)
    result = monica_client.find_contact(c.get("first_name"))

    assert result is not None


def test_create_note(monica_client, random_name, default_gender):
    c = monica_client.create_contact(random_name, default_gender)

    assert c is not None

    note = monica_client.create_note("my note", c.get("id"))
    assert note is not None


def test_genders(monica_client):
    result = monica_client.genders()

    assert len(result) > 0
