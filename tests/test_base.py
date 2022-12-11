from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from app import models
from app.crud import CRUD
from app.manager import ConnManager
from main import app


@pytest.fixture(scope='session', autouse=True)
def queries() -> CRUD:
    # INIT db and destroy all data / tables after.
    ConnManager().drop_tables_if_exist()
    ConnManager().define_tables()
    yield CRUD()


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

def test_api():
    client = TestClient(app)
    assert client.get('/products').status_code == 200
    assert client.get('/categories').status_code == 200
    assert client.get('/both').status_code == 200
