from fastapi import FastAPI, status

from app import schemas
from app.crud import CRUD
from app.manager import ConnManager

app = FastAPI()
crud = CRUD()


@app.on_event("startup")
def startup():
    ConnManager().drop_tables_if_exist()
    ConnManager().define_tables()
    crud._fake_populate_products_categories()  # pylint: disable=protected-access
    crud._fake_populate_junction_table()  # pylint: disable=protected-access


@app.on_event("shutdown")
def shutdown():
    ConnManager().drop_tables()


@app.get("/products",  status_code=status.HTTP_200_OK, response_model=list[schemas.Product])
def get_products_and_its_categories():
    return crud.get_products()


@app.get("/categories", status_code=status.HTTP_200_OK, response_model=list[schemas.Category])
def get_categories_and_its_products():
    return crud.get_categories()


@app.get("/both", status_code=status.HTTP_200_OK, response_model=list[schemas.ProductCategory])
def get_product_category_pairs():
    return crud.get_products_and_categories()
