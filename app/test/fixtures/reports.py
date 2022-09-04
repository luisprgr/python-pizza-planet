import pytest
from datetime import datetime
from app.repositories.managers import (
    IngredientManager,
    SizeManager,
    BeverageManager,
    OrderManager,
)


def __search_id_by_name(name, items):
    for item in items:
        if item.get('name') == name:
            return item.get('_id')
    return None


@pytest.fixture
def reports_uri():
    return "/report/"


@pytest.fixture
def reports_sizes(app, reports_data_sizes):
    return [SizeManager.create(size) for size in reports_data_sizes]


@pytest.fixture
def reports_ingredients(app, reports_data_ingredients):
    return [
        IngredientManager.create(ingredient)
        for ingredient in reports_data_ingredients
    ]


@pytest.fixture
def reports_beverages(app, reports_data_beverages):
    return [
        BeverageManager.create(beverage) for beverage in reports_data_beverages
    ]


@pytest.fixture
def reports_orders(
    app,
    reports_sizes,
    reports_ingredients,
    reports_beverages,
    reports_data_orders,
):
    orders = []
    for order in reports_data_orders:
        (ingredient_detail, beverage_detail) = order.pop("detail")
        ingredient_id = __search_id_by_name(
            ingredient_detail["ingredient"]['name'], reports_ingredients
        )
        beverage_id = __search_id_by_name(
            beverage_detail["beverage"]['name'], reports_beverages
        )
        size_id = __search_id_by_name(order.pop("size")['name'], reports_sizes)
        ingredients = IngredientManager.get_by_id_list([ingredient_id])
        beverages = BeverageManager.get_by_id_list([beverage_id])
        order["date"] = datetime.fromisoformat(order["date"])
        orders.append(
            OrderManager.create(
                order | {'size_id': size_id}, ingredients, beverages
            )
        )
    return orders


@pytest.fixture
def report_values():
    return {
        "most_requested_ingredient": {
            "name": "Green Peppers",
            "times_requested": 4,
        },
        "most_requested_beverage": {"name": "Sprite", "times_requested": 4},
        "month_with_more_revenue": {"name": "March", "total_revenue": 68.15},
        "top_3_customers": [
            {
                "dni": "01234567891",
                "name": "Christopher Sandoval",
                "address": "fake address",
                "phone": "123456789",
                "spent": 70.46,
            },
            {
                "dni": "01234567893",
                "name": "Kelly Cook",
                "address": "fake address",
                "phone": "123456789",
                "spent": 17.08,
            },
            {
                "dni": "01234567892",
                "name": "Teresa Nelson",
                "address": "fake address",
                "phone": "123456789",
                "spent": 14.29,
            },
        ],
    }
