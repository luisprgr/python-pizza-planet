import pytest
from datetime import datetime
from app.repositories.managers import (
    IngredientManager,
    SizeManager,
    BeverageManager,
    OrderManager,
)


@pytest.fixture
def reports_uri():
    return "/report/"


@pytest.fixture
def reports_sizes(reports_data_sizes):
    map(SizeManager.create, reports_data_sizes)


@pytest.fixture
def reports_ingredients(reports_data_ingredients):
    map(IngredientManager.create, reports_data_ingredients)


@pytest.fixture
def reports_beverages(reports_data_beverages):
    map(BeverageManager.create, reports_data_beverages)


@pytest.fixture
def reports_orders(reports_sizes, reports_ingredients, reports_beverages, reports_data_orders):
    orders = []
    for order in reports_data_orders:
        (ingredient_detail, beverage_detail) = order.pop("detail")
        size_id = order.pop("size")["_id"]
        order["date"] = datetime.fromisoformat(order["date"])
        orders.append(
            OrderManager.create(
                order | {'size_id': size_id}, [ingredient_detail["ingredient"]], [beverage_detail["beverage"]]
            )
        )
    return orders
