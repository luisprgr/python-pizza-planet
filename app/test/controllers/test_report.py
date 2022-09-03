import pytest
from app.controllers import (
    ReportController,
)


def test_create(
    app, reports_sizes, reports_ingredients, reports_beverages, reports_orders
):

    report = ReportController.get_report()
    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['most_requested_beverage'])
    pytest.assume(report['month_with_more_revenue'])
    pytest.assume(report['top_3_customers'])

    pytest.assume(
        report['most_requested_ingredient']['name'] == 'Green Peppers'
    )
    pytest.assume(report['most_requested_ingredient']['times_requested'] == 4)

    pytest.assume(report['most_requested_beverage']['name'] == 'Sprite')
    pytest.assume(report['most_requested_beverage']['times_requested'] == 4)

    pytest.assume(report['month_with_more_revenue'] == 'March')

    pytest.assume(report['top_3_customers'][0]['dni'] == '01234567891')
    pytest.assume(
        report['top_3_customers'][0]['name'] == 'Christopher Sandoval'
    )
    pytest.assume(report['top_3_customers'][0]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][0]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][0]['spent'] == 70.07)

    pytest.assume(report['top_3_customers'][1]['dni'] == '01234567893')
    pytest.assume(report['top_3_customers'][1]['name'] == 'Kelly Cook')
    pytest.assume(report['top_3_customers'][1]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][1]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][1]['spent'] == 17.08)

    pytest.assume(report['top_3_customers'][2]['dni'] == '01234567892')
    pytest.assume(report['top_3_customers'][2]['name'] == 'Teresa Nelson')
    pytest.assume(report['top_3_customers'][2]['address'] == 'fake address')
    pytest.assume(report['top_3_customers'][2]['phone'] == '123456789')
    pytest.assume(report['top_3_customers'][2]['spent'] == 14.29)
