from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from app.services.service_decorator import service

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
@service
def create_ingredient():
    return IngredientController.create(request.json)


@ingredient.route('/', methods=PUT)
@service
def update_ingredient():
    return IngredientController.update(request.json)


@ingredient.route('/id/<_id>', methods=GET)
@service
def get_ingredient_by_id(_id: int):
    return IngredientController.get_by_id(_id)


@ingredient.route('/', methods=GET)
@service
def get_ingredients():
    return IngredientController.get_all()
