from pydantic import BaseModel, validator, Field

from . import models


class ProductBase(BaseModel):
    value: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    value: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    value: str
    categories: list[object]

    @validator('categories', each_item=True)
    def retrieve_all_categories(cls, v: models.ProductCategory):
        return v.categories.value

    class Config:
        orm_mode = True


class Category(BaseModel):
    value: str
    products: list[object]

    @validator('products', each_item=True)
    def retrieve_all_products(cls, v: models.ProductCategory):
        return v.products.value

    class Config:
        orm_mode = True


class ProductCategory(BaseModel):
    products: object = Field(..., alias="product")
    categories: object = Field(..., alias="category")

    @validator('products')
    def retrieve_product_value(cls, v: models.Product):
        return v.value

    @validator('categories')
    def retrieve_category_value(cls, v: models.Category):
        return v.value

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
