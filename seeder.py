from app.repositories.managers import (
    SizeManager,
    BeverageManager,
    OrderManager,
    IngredientManager,
)
from faker import Faker

# - At least 100 orders with different customers
# - A customer should have multiple orders
# - the data should be created for multiple months

MAX_LEFT_DIGITS = 2
MAX_RIGHT_DIGITS = 2
MAX_ORDERS = 100

INGREDIENT_MAX_VALUE = 5.00
INGREDIENT_MIN_VALUE = 1.00

BEVERAGE_MAX_VALUE = 5.00
BEVERAGE_MIN_VALUE = 0.50

fake = Faker()

sizes = [
    {
        'name': 'personal',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=1,
            max_value=5,
        )
    },
    {
        'name': 'medium',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=5,
            max_value=10,
        )
    },
    {
        'name': 'familiar',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=10,
            max_value=15,
        )
    },
    {
        'name': 'large',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=15,
            max_value=20,
        )
    },
    {
        'name': 'extra large',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=20,
            max_value=25,
        )
    },
]

ingredients = [
    {
        'name': 'Jalapeño',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Green Peppers',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Tomato',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Cheese',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Mushrooms',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Chicken',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Oregano',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Bacon',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Pepperoni',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
    {
        'name': 'Sausage',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=INGREDIENT_MIN_VALUE,
            max_value=INGREDIENT_MAX_VALUE,
        )
    },
]

beverages = [
    {
        'name': 'Coca Cola',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=BEVERAGE_MIN_VALUE,
            max_value=BEVERAGE_MAX_VALUE,
        )
    },
    {
        'name': 'Fanta',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=BEVERAGE_MIN_VALUE,
            max_value=BEVERAGE_MAX_VALUE,
        )
    },
    {
        'name': 'Sprite',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=BEVERAGE_MIN_VALUE,
            max_value=BEVERAGE_MAX_VALUE,
        )
    },
    {
        'name': 'Pepsi',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=BEVERAGE_MIN_VALUE,
            max_value=BEVERAGE_MAX_VALUE,
        )
    },
    {
        'name': 'Water',
        'price': fake.pyfloat(
            left_digits=MAX_LEFT_DIGITS,
            right_digits=MAX_RIGHT_DIGITS,
            positive=True,
            min_value=BEVERAGE_MIN_VALUE,
            max_value=BEVERAGE_MAX_VALUE,
        )
    },
]


def generate_client():
    return {
        'client_address': fake.address(),
        'client_dni': fake.ssn(),
        'client_name': fake.name(),
        'client_phone': fake.phone_number(),
    }

def seed_size_table():
    for size in sizes:
        SizeManager.create(size)

def seed_ingredient_table():
    for ingredient in ingredients:
        IngredientManager.create(ingredient)

def seed_beverage_table():
    for beverage in beverages:
        BeverageManager.create(beverage)

def get_sizes_ingredients_beverages():
    return {
        'sizes': SizeManager.get_all(),
        'ingredients': IngredientManager.get_all(),
        'beverages': BeverageManager.get_all(),
    }



def execute_seeder():
    seed_size_table()
    seed_ingredient_table()
    seed_beverage_table()
    print(get_sizes_ingredients_beverages())
