from flask import Blueprint, jsonify, request
from app.controllers.base import BaseController
from app.common.http_methods import GET, POST, PUT

class ServiceBuilder:
    result: Blueprint = None
    controller: BaseController = None
    name: str = None
    import_name: str = None

    @classmethod
    def build_create_method(cls):
        item, error = cls.controller.create(request.json)
        response = item if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def build_update_method(cls, _id: int):
        item, error = cls.controller.update({"_id": _id} | request.json)
        response = item if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def build_get_by_id_method(cls, _id: int):
        item, error = cls.controller.get_by_id(_id)
        response = item if not error else {'error': error}
        status_code = 200 if item else 404 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def build_get_all_method(cls):
        items, error = cls.controller.get_all()
        response = items if not error else {'error': error}
        status_code = 200 if items else 404 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def build(cls):
        cls.result = Blueprint(cls.name, cls.import_name)
        cls.result.add_url_rule(
            '/', methods=POST , view_func=cls.build_create_method
        )
        cls.result.add_url_rule(
            '/<_id>', methods=PUT, view_func=cls.build_update_method
        )
        cls.result.add_url_rule(
            '/id/<_id>', methods=GET, view_func=cls.build_get_by_id_method
        )
        cls.result.add_url_rule(
            '/', methods=GET, view_func=cls.build_get_all_method
        )
        return cls.result
