from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from app import models
from app.crud import CRUD
from app.manager import ConnManager
from bucket_generator import generate_session_id
from main import app


@pytest.fixture(scope='session', autouse=True)
def queries() -> CRUD:
    # INIT db and destroy all data / tables after.
    ConnManager().drop_tables_if_exist()
    ConnManager().define_tables()
    yield CRUD()
    ConnManager().drop_tables()


def test_crud_populate(queries: CRUD):
    queries._fake_populate_products_categories(n_products=10)
    queries._fake_populate_junction_table()
    assert len(queries.get_products()) == 10, queries.get_products()


def test_crud_get_products(queries: CRUD):
    q = queries.get_products()
    assert type(q) is list
    assert type(q[0]) == models.Product


def test_crud_get_categories(queries: CRUD):
    q = queries.get_categories()
    assert type(q) is list
    assert type(q[0]) == models.Category


def test_crud_get_products_categories(queries: CRUD):
    q = queries.get_products_and_categories()
    assert type(q) is list
    assert type(q[0]) == models.ProductCategory


def test_bucket_generator():
    # Should have same session id
    time1 = datetime(2022, 11, 11, 11, 1).timestamp()
    time2 = datetime(2022, 11, 11, 11, 2).timestamp()

    # Should have different session id
    time3 = datetime(2022, 11, 11, 11, 4).timestamp()

    session_id_1 = generate_session_id(time1)
    session_id_2 = generate_session_id(time2)
    session_id_3 = generate_session_id(time3)

    assert session_id_1 == session_id_2 != session_id_3


def test_bucket_generator_2():
    # In 1 hour there might only be 20 sessions 3 minute sessions
    session_ids = []

    t = datetime(2022, 11, 11, 11, 0)
    for minute in range(60):
        session_ids.append(
            generate_session_id(
                (t + timedelta(minutes=minute)).timestamp()
            )
        )
    assert len(session_ids) == 60


def test_api():
    client = TestClient(app)
    assert client.get('/products').status_code == 200
    assert client.get('/categories').status_code == 200
    assert client.get('/both').status_code == 200
