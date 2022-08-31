import pytest


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith("200"))
    returned_sizes = {size["_id"]: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size["_id"] in returned_sizes)


def test_create_size_service(client, size_uri, size):
    response = client.post(size_uri, json=size)
    pytest.assume(response.status.startswith("200"))
    returned_size = response.json
    pytest.assume(returned_size["_id"])
    pytest.assume(returned_size["name"] == size["name"])
    pytest.assume(returned_size["price"] == size["price"])


def test_update_size_service(client, create_size, size_uri, size):
    size_id = create_size.json["_id"]
    response = client.put(f'{size_uri}{size_id}', json=size)
    pytest.assume(response.status.startswith("200"))
    returned_size = response.json
    pytest.assume(returned_size["_id"] == create_size.json["_id"])
    pytest.assume(returned_size["name"] == size["name"])
    pytest.assume(returned_size["price"] == size["price"])

def test_get_size_by_id_service(client, create_size, size_uri):
    size_id = create_size.json["_id"]
    response = client.get(f'{size_uri}id/{size_id}')
    pytest.assume(response.status.startswith("200"))
    returned_size = response.json
    pytest.assume(returned_size["_id"] == create_size.json["_id"])
    pytest.assume(returned_size["name"] == create_size.json["name"])
    pytest.assume(returned_size["price"] == create_size.json["price"])
