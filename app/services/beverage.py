from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from app.services.service_decorator import service

beverage = Blueprint("beverage", __name__)


@beverage.route("/", methods=POST)
@service
def create_beverage():
    return BeverageController.create(request.json)


@beverage.route("/<_id>", methods=PUT)
@service
def update_beverage(_id: int):
    return BeverageController.update({"_id": _id} | request.json)


@beverage.route("/id/<_id>", methods=GET)
@service
def get_beverage_by_id(_id: int):
    return BeverageController.get_by_id(_id)


@beverage.route("/", methods=GET)
@service
def get_beverages():
    return BeverageController.get_all()
