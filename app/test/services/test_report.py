import pytest


def test_get_report(
    client,
    reports_sizes,
    reports_ingredients,
    reports_beverages,
    reports_orders,
    report_values,
    reports_uri,
):
    response = client.get(reports_uri)

    pytest.assume(response.status_code == 200)
    pytest.assume(response.json['most_requested_ingredient'])
    pytest.assume(response.json['most_requested_beverage'])
    pytest.assume(response.json['month_with_more_revenue'])
    pytest.assume(response.json['top_3_customers'])

    pytest.assume(
        response.json['most_requested_ingredient']['name']
        == report_values['most_requested_ingredient']['name']
    )
    pytest.assume(
        response.json['most_requested_ingredient']['times_requested']
        == report_values['most_requested_ingredient']['times_requested']
    )

    pytest.assume(
        response.json['most_requested_beverage']['name']
        == report_values['most_requested_beverage']['name']
    )
    pytest.assume(
        response.json['most_requested_beverage']['times_requested']
        == report_values['most_requested_beverage']['times_requested']
    )

    pytest.assume(
        response.json['month_with_more_revenue']['name']
        == report_values['month_with_more_revenue']['name']
    )
    pytest.assume(
        response.json['month_with_more_revenue']['total_revenue']
        == report_values['month_with_more_revenue']['total_revenue']
    )

    pytest.assume(
        response.json['top_3_customers'][0]['dni']
        == report_values['top_3_customers'][0]['dni']
    )
    pytest.assume(
        response.json['top_3_customers'][0]['name']
        == report_values['top_3_customers'][0]['name']
    )
    pytest.assume(
        response.json['top_3_customers'][0]['address']
        == report_values['top_3_customers'][0]['address']
    )
    pytest.assume(
        response.json['top_3_customers'][0]['phone']
        == report_values['top_3_customers'][0]['phone']
    )
    pytest.assume(
        response.json['top_3_customers'][0]['spent']
        == report_values['top_3_customers'][0]['spent']
    )

    pytest.assume(
        response.json['top_3_customers'][1]['dni']
        == report_values['top_3_customers'][1]['dni']
    )
    pytest.assume(
        response.json['top_3_customers'][1]['name']
        == report_values['top_3_customers'][1]['name']
    )
    pytest.assume(
        response.json['top_3_customers'][1]['address']
        == report_values['top_3_customers'][1]['address']
    )
    pytest.assume(
        response.json['top_3_customers'][1]['phone']
        == report_values['top_3_customers'][1]['phone']
    )
    pytest.assume(
        response.json['top_3_customers'][1]['spent']
        == report_values['top_3_customers'][1]['spent']
    )

    pytest.assume(
        response.json['top_3_customers'][2]['dni']
        == report_values['top_3_customers'][2]['dni']
    )
    pytest.assume(
        response.json['top_3_customers'][2]['name']
        == report_values['top_3_customers'][2]['name']
    )
    pytest.assume(
        response.json['top_3_customers'][2]['address']
        == report_values['top_3_customers'][2]['address']
    )
    pytest.assume(
        response.json['top_3_customers'][2]['phone']
        == report_values['top_3_customers'][2]['phone']
    )
    pytest.assume(
        response.json['top_3_customers'][2]['spent']
        == report_values['top_3_customers'][2]['spent']
    )
