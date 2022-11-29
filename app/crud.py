import random

from sqlalchemy import select

from . import models
from .manager import ConnManager


class CRUD:
    """Convenience class, all methods bundled toghether for simplified unit tests and API usage."""

    def __init__(self) -> None:
        self.session = ConnManager().session

    def _fake_populate_products_categories(  # pylint: disable=dangerous-default-value
        self,
        n_products: int = 30,
        categories: list[str] = [
            "Category_A",
            "Category_B",
            "Category_C",
            "Category_D",
        ],
    ) -> None:
        from faker import Faker

        faker = Faker()

        products = [
            models.Product(value=faker.catch_phrase()) for i in range(n_products)
        ]
        categories = [models.Category(value=category) for category in categories]

        self.session.bulk_save_objects(products + categories)  # deprecated
        self.session.commit()

    def _fake_populate_junction_table(self):
        products = self.get_products()
        categories = self.get_categories()

        assert len(products) > 1 and len(categories) > 1

        m2m = []
        # Assign category to each product, except for last 30%
        for product in products[2 : -len(products) * 3 // 10]:
            # Each product shall have at least 1 and at most 3 categories
            for category in set(random.choices(categories, k=len(categories))):
                m2m.append(
                    models.ProductCategory(
                        product_pk=product.id, category_pk=category.id
                    )
                )

        self.session.bulk_save_objects(m2m)
        self.session.commit()

        empty_category = models.Category(value="EmptyCategory")
        self.session.add(empty_category)
        self.session.commit()

    def get_products(self) -> list[models.Product]:
        result = self.session.execute(select(models.Product))
        return result.scalars().all()

    def get_categories(self) -> list[models.Category]:
        result = self.session.execute(select(models.Category))
        return result.scalars().all()

    def get_products_and_categories(self):
        result = self.session.execute(select(models.ProductCategory))
        return result.scalars().all()
