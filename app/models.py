from sqlalchemy import Column, ForeignKey, Integer, String, Identity
from sqlalchemy.orm import relationship

from .default_connection import Base


class ProductCategory(Base):
    __tablename__ = "product_category"
    product_pk = Column(ForeignKey("product_table.id"), primary_key=True)
    category_pk = Column(ForeignKey("category_table.id"), primary_key=True)

    products = relationship("Product", back_populates="categories")
    categories = relationship("Category", back_populates="products")


class Product(Base):
    __tablename__ = "product_table"
    id = Column(
        Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True
    )
    value = Column(String)

    categories = relationship("ProductCategory", back_populates="products")


class Category(Base):
    __tablename__ = "category_table"
    id = Column(
        Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True
    )
    value = Column(String)

    products = relationship("ProductCategory", back_populates="categories")
