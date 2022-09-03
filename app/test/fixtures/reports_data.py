import pytest

__orders = [
    {
        "_id": 1,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-03-02T19:15:04",
        "detail": [
            {
                "_id": 1,
                "beverage": None,
                "ingredient": {
                    "_id": 2,
                    "name": "Green Peppers",
                    "price": 4.5,
                },
                "total_detail_price": 4.5,
            },
            {
                "_id": 2,
                "beverage": {"_id": 1, "name": "Coca Cola", "price": 2.34},
                "ingredient": None,
                "total_detail_price": 2.34,
            },
        ],
        "size": {"_id": 1, "name": "personal", "price": 2.67},
        "total_price": 9.51,
    },
    {
        "_id": 2,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-03-02T19:15:04",
        "detail": [
            {
                "_id": 3,
                "beverage": None,
                "ingredient": {
                    "_id": 2,
                    "name": "Green Peppers",
                    "price": 4.5,
                },
                "total_detail_price": 4.5,
            },
            {
                "_id": 4,
                "beverage": {"_id": 3, "name": "Sprite", "price": 0.45},
                "ingredient": None,
                "total_detail_price": 0.45,
            },
        ],
        "size": {"_id": 3, "name": "familiar", "price": 10.69},
        "total_price": 15.63,
    },
    {
        "_id": 3,
        "client_address": "fake address",
        "client_dni": "01234567892",
        "client_name": "Teresa Nelson",
        "client_phone": "123456789",
        "date": "2022-03-02T19:15:04",
        "detail": [
            {
                "_id": 5,
                "beverage": None,
                "ingredient": {"_id": 1, "name": "Jalapeño", "price": 3.16},
                "total_detail_price": 3.16,
            },
            {
                "_id": 6,
                "beverage": {"_id": 3, "name": "Sprite", "price": 0.45},
                "ingredient": None,
                "total_detail_price": 0.45,
            },
        ],
        "size": {"_id": 3, "name": "familiar", "price": 10.69},
        "total_price": 14.29,
    },
    {
        "_id": 4,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-11-12T10:10:32",
        "detail": [
            {
                "_id": 7,
                "beverage": None,
                "ingredient": {
                    "_id": 2,
                    "name": "Green Peppers",
                    "price": 4.5,
                },
                "total_detail_price": 4.5,
            },
            {
                "_id": 8,
                "beverage": {"_id": 1, "name": "Coca Cola", "price": 2.34},
                "ingredient": None,
                "total_detail_price": 2.34,
            },
        ],
        "size": {"_id": 2, "name": "medium", "price": 5.86},
        "total_price": 12.7,
    },
    {
        "_id": 5,
        "client_address": "fake address",
        "client_dni": "01234567893",
        "client_name": "Kelly Cook",
        "client_phone": "123456789",
        "date": "2022-05-01T23:36:22",
        "detail": [
            {
                "_id": 9,
                "beverage": None,
                "ingredient": {"_id": 1, "name": "Jalapeño", "price": 3.16},
                "total_detail_price": 3.16,
            },
            {
                "_id": 10,
                "beverage": {"_id": 2, "name": "Fanta", "price": 2.28},
                "ingredient": None,
                "total_detail_price": 2.28,
            },
        ],
        "size": {"_id": 2, "name": "medium", "price": 5.86},
        "total_price": 11.29,
    },
    {
        "_id": 6,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-11-12T10:10:32",
        "detail": [
            {
                "_id": 11,
                "beverage": None,
                "ingredient": {"_id": 3, "name": "Tomato", "price": 2.67},
                "total_detail_price": 2.67,
            },
            {
                "_id": 12,
                "beverage": {"_id": 2, "name": "Fanta", "price": 2.28},
                "ingredient": None,
                "total_detail_price": 2.28,
            },
        ],
        "size": {"_id": 2, "name": "medium", "price": 5.86},
        "total_price": 10.81,
    },
    {
        "_id": 7,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-11-12T10:10:32",
        "detail": [
            {
                "_id": 13,
                "beverage": None,
                "ingredient": {"_id": 3, "name": "Tomato", "price": 2.67},
                "total_detail_price": 2.67,
            },
            {
                "_id": 14,
                "beverage": {"_id": 3, "name": "Sprite", "price": 0.45},
                "ingredient": None,
                "total_detail_price": 0.45,
            },
        ],
        "size": {"_id": 1, "name": "personal", "price": 2.67},
        "total_price": 5.79,
    },
    {
        "_id": 8,
        "client_address": "fake address",
        "client_dni": "01234567894",
        "client_name": "Lindsay Conley",
        "client_phone": "123456789",
        "date": "2022-03-02T19:15:04",
        "detail": [
            {
                "_id": 15,
                "beverage": None,
                "ingredient": {
                    "_id": 2,
                    "name": "Green Peppers",
                    "price": 4.5,
                },
                "total_detail_price": 4.5,
            },
            {
                "_id": 16,
                "beverage": {"_id": 1, "name": "Coca Cola", "price": 2.34},
                "ingredient": None,
                "total_detail_price": 2.34,
            },
        ],
        "size": {"_id": 2, "name": "medium", "price": 5.86},
        "total_price": 12.7,
    },
    {
        "_id": 9,
        "client_address": "fake address",
        "client_dni": "01234567893",
        "client_name": "Kelly Cook",
        "client_phone": "123456789",
        "date": "2022-05-01T23:36:22",
        "detail": [
            {
                "_id": 17,
                "beverage": None,
                "ingredient": {"_id": 3, "name": "Tomato", "price": 2.67},
                "total_detail_price": 2.67,
            },
            {
                "_id": 18,
                "beverage": {"_id": 3, "name": "Sprite", "price": 0.45},
                "ingredient": None,
                "total_detail_price": 0.45,
            },
        ],
        "size": {"_id": 1, "name": "personal", "price": 2.67},
        "total_price": 5.79,
    },
    {
        "_id": 10,
        "client_address": "fake address",
        "client_dni": "01234567891",
        "client_name": "Christopher Sandoval",
        "client_phone": "123456789",
        "date": "2022-03-02T19:15:04",
        "detail": [
            {
                "_id": 19,
                "beverage": None,
                "ingredient": {"_id": 3, "name": "Tomato", "price": 2.67},
                "total_detail_price": 2.67,
            },
            {
                "_id": 20,
                "beverage": {"_id": 2, "name": "Fanta", "price": 2.28},
                "ingredient": None,
                "total_detail_price": 2.28,
            },
        ],
        "size": {"_id": 3, "name": "familiar", "price": 10.69},
        "total_price": 15.63,
    },
]

__ingredients = [
    {"name": "Jalapeño", "price": 3.16},
    {"name": "Green Peppers", "price": 4.5},
    {"name": "Tomato", "price": 2.67},
]

__beverages = [
    {"name": "Coca Cola", "price": 2.34},
    {"name": "Fanta", "price": 2.28},
    {"name": "Sprite", "price": 0.45},
]

__sizes = [
    {"name": "personal", "price": 2.67},
    {"name": "medium", "price": 5.86},
    {"name": "familiar", "price": 10.69},
]


@pytest.fixture
def reports_data_orders():
    return __orders


@pytest.fixture
def reports_data_ingredients():
    return __ingredients


@pytest.fixture
def reports_data_beverages():
    return __beverages


@pytest.fixture
def reports_data_sizes():
    return __sizes
