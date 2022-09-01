import pytest


def test_get_beverages_service(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)
    pytest.assume(response.status.startswith("200"))
    returned_beverages = {
        beverage["_id"]: beverage for beverage in response.json
    }
    for beverage in create_beverages:
        pytest.assume(beverage["_id"] in returned_beverages)


def test_create_beverage_service(client, beverage, beverage_uri):
    response = client.post(beverage_uri, json=beverage)
    pytest.assume(response.status.startswith("200"))
    returned_beverage = response.json
    pytest.assume(returned_beverage["_id"])
    pytest.assume(returned_beverage["name"] == beverage["name"])
    pytest.assume(returned_beverage["price"] == beverage["price"])


def test_update_beverage_service(
    client, create_beverage, beverage, beverage_uri
):
    beverage_id = create_beverage.json["_id"]
    response = client.put(f'{beverage_uri}{beverage_id}', json=beverage)
    pytest.assume(response.status.startswith("200"))
    returned_beverage = response.json
    pytest.assume(returned_beverage["_id"] == create_beverage.json["_id"])
    pytest.assume(returned_beverage["name"] == beverage["name"])
    pytest.assume(returned_beverage["price"] == beverage["price"])


def test_get_beverage_by_id_service(client, create_beverage, beverage_uri):
    beverage_id = create_beverage.json["_id"]
    response = client.get(f'{beverage_uri}id/{beverage_id}')
    pytest.assume(response.status.startswith("200"))
    returned_beverage = response.json
    pytest.assume(returned_beverage["_id"] == create_beverage.json["_id"])
    pytest.assume(returned_beverage["name"] == create_beverage.json["name"])
    pytest.assume(returned_beverage["price"] == create_beverage.json["price"])
