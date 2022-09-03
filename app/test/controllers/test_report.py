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

def __get_customers(orders):
    return reduce(
        operator.ior,
        map(
            lambda order: {
                order["client_dni"]: {
                    'name': order['client_name'],
                    'address': order['client_address'],
                    'phone': order['client_phone'],
                    'spent': 0,
                }
            },
            orders,
        ),
        {},
    )

def __get_top_customers(customers, orders):
    for order in orders:
        customers[order['client_dni']]['spent'] += order['total_price']
    return sorted(
        customers.values(), key=lambda customer: customer['spent'], reverse=True
    )[:3]

def __get_most_requested_ingredient(ingredients, orders):
    ingredients = {ingredient['name']: 0 for ingredient in ingredients}
    for order in orders:
        for detail in order['detail']:
            if detail['ingredient']:
                ingredients[detail['ingredient']['name']] += 1
    return sorted(
        ingredients.items(), key=lambda ingredient: ingredient[1], reverse=True
    )[0]

def __get_most_requested_beverage(beverages, orders):
    beverages = {beverage['name']:0 for beverage in beverages}
    for order in orders:
        for detail in order['detail']:
            if detail['beverage']:
                beverages[detail["beverage"]["name"]] += 1
    return sorted(beverages.items(), key=lambda x: x[1], reverse=True)[0]

def __get_months(orders):
    return reduce(
        operator.ior,
        map(
            lambda order: {
                order["date"]: 0,
                },
            orders,
        ),
        {},
    )

def __month_with_more_revenue(months, orders):
    for order in orders:
        months[order['date']] += order['total_price']
    return sorted(months.items(), key=lambda x: x[1], reverse=True)[0]

def test_create(app, reports_sizes, reports_ingredients, reports_beverages, reports_orders):
    customers = __get_customers(reports_orders)
    top_customers = __get_top_customers(customers, reports_orders)
    most_requested_ingredient = __get_most_requested_ingredient(reports_ingredients, reports_orders)
    most_requested_beverage = __get_most_requested_beverage(reports_beverages, reports_orders)
    months = __get_months(reports_orders)
    month_with_more_revenue = __month_with_more_revenue(months, reports_orders)

    a = 1 #point to set a breakpoint


    report = ReportController.get_report()
    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['most_requested_beverage'])
    pytest.assume(report['month_with_more_revenue'])
    pytest.assume(report['top_3_customers'])
    
    pytest.assume(report['most_requested_ingredient']['name'] == 'ingredient 1')
    pytest.assume(report['most_requested_ingredient']['times_requested'] == 2)
    pytest.assume(report['most_requested_beverage']['name'] == 'beverage 1')
    pytest.assume(report['most_requested_beverage']['times_requested'] == 2)

    pytest.assume(report['month_with_more_revenue'] == '2020-01')
    
    pytest.assume(report['top_3_customers'][0]['dni'] == '0123456789')
    pytest.assume(report['top_3_customers'][0]['name'] == 'client')
    pytest.assume(report['top_3_customers'][0]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][0]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][0]['spent'] == 100)
    
    pytest.assume(report['top_3_customers'][1]['dni'] == '0123456789')
    pytest.assume(report['top_3_customers'][1]['name'] == 'client')
    pytest.assume(report['top_3_customers'][1]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][1]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][1]['spent'] == 100)
    
    pytest.assume(report['top_3_customers'][2]['dni'] == '0123456789')
    pytest.assume(report['top_3_customers'][2]['name'] == 'client')
    pytest.assume(report['top_3_customers'][2]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][2]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][2]['spent'] == 100)
    
    
