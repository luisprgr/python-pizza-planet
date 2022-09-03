from functools import reduce
import operator
import pytest
from app.controllers import (
    # ReportController,
    IngredientController,
    BeverageController,
    SizeController,
    OrderController,
)

# - Which is the most requested ingredient
# - Which is the month with more revenue
# - We want to reward our best customers,
#   so we would like to know who are the
#   top 3 customers (those who buy more).

def __get_customers(orders):
    return reduce(
        operator.ior,
        map(
            lambda order: {
                order.json["client_dni"]: {
                    'name': order.json['client_name'],
                    'spent': 0,
                }
            },
            orders,
        ),
        {},
    )




def test_create(app, reports_sizes, reports_ingredients, reports_beverages, reports_orders):
    orders = reports_orders
    
