from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from app.services.service_decorator import service

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
@service
def create_size():
    return SizeController.create(request.json)


@size.route('/<_id>', methods=PUT)
@service
def update_size(_id: int):
    return SizeController.update({"_id": _id} | request.json)


@size.route('/id/<_id>', methods=GET)
@service
def get_size_by_id(_id: int):
    return SizeController.get_by_id(_id)


@size.route('/', methods=GET)
@service
def get_sizes():
    return SizeController.get_all()
