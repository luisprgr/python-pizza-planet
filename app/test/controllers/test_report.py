import pytest
from app.controllers import (
    ReportController,
)


def test_create(
    app,
    reports_sizes,
    reports_ingredients,
    reports_beverages,
    reports_orders,
    report_values,
):

    report, _ = ReportController.get_report()

    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['most_requested_beverage'])
    pytest.assume(report['month_with_more_revenue'])
    pytest.assume(report['top_3_customers'])

    pytest.assume(
        report['most_requested_ingredient']['name']
        == report_values['most_requested_ingredient']['name']
    )
    pytest.assume(
        report['most_requested_ingredient']['times_requested']
        == report_values['most_requested_ingredient']['times_requested']
    )

    pytest.assume(
        report['most_requested_beverage']['name']
        == report_values['most_requested_beverage']['name']
    )
    pytest.assume(
        report['most_requested_beverage']['times_requested']
        == report_values['most_requested_beverage']['times_requested']
    )

    pytest.assume(
        report['month_with_more_revenue']['name']
        == report_values['month_with_more_revenue']['name']
    )
    pytest.assume(
        report['month_with_more_revenue']['total_revenue']
        == report_values['month_with_more_revenue']['total_revenue']
    )

    pytest.assume(
        report['top_3_customers'][0]['dni']
        == report_values['top_3_customers'][0]['dni']
    )
    pytest.assume(
        report['top_3_customers'][0]['name']
        == report_values['top_3_customers'][0]['name']
    )
    pytest.assume(
        report['top_3_customers'][0]['address']
        == report_values['top_3_customers'][0]['address']
    )
    pytest.assume(
        report['top_3_customers'][0]['phone']
        == report_values['top_3_customers'][0]['phone']
    )
    pytest.assume(
        report['top_3_customers'][0]['spent']
        == report_values['top_3_customers'][0]['spent']
    )

    pytest.assume(
        report['top_3_customers'][1]['dni']
        == report_values['top_3_customers'][1]['dni']
    )
    pytest.assume(
        report['top_3_customers'][1]['name']
        == report_values['top_3_customers'][1]['name']
    )
    pytest.assume(
        report['top_3_customers'][1]['address']
        == report_values['top_3_customers'][1]['address']
    )
    pytest.assume(
        report['top_3_customers'][1]['phone']
        == report_values['top_3_customers'][1]['phone']
    )
    pytest.assume(
        report['top_3_customers'][1]['spent']
        == report_values['top_3_customers'][1]['spent']
    )

    pytest.assume(
        report['top_3_customers'][2]['dni']
        == report_values['top_3_customers'][2]['dni']
    )
    pytest.assume(
        report['top_3_customers'][2]['name']
        == report_values['top_3_customers'][2]['name']
    )
    pytest.assume(
        report['top_3_customers'][2]['address']
        == report_values['top_3_customers'][2]['address']
    )
    pytest.assume(
        report['top_3_customers'][2]['phone']
        == report_values['top_3_customers'][2]['phone']
    )
    pytest.assume(
        report['top_3_customers'][2]['spent']
        == report_values['top_3_customers'][2]['spent']
    )
