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
