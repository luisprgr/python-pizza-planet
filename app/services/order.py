from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..controllers import OrderController
from app.services.service_decorator import service

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
@service
def create_order():
    return OrderController.create(request.json)


@order.route('/id/<_id>', methods=GET)
@service
def get_order_by_id(_id: int):
    return OrderController.get_by_id(_id)


@order.route('/', methods=GET)
@service
def get_orders():
    return OrderController.get_all()
