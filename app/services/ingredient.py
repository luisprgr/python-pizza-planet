from flask import request, jsonify
from app.common.http_methods import PUT
from ..controllers import IngredientController
from .service_builder import ServiceBuilder


class IngredientServiceBuilder(ServiceBuilder):
    controller = IngredientController
    name = 'ingredient'
    import_name = __name__

    @classmethod
    def build_update_method(cls):
        def update_ingredient():
            ingredient, error = IngredientController.update(request.json)
            response = ingredient if not error else {'error': error}
            status_code = 200 if not error else 400
            return jsonify(response), status_code

        cls.result.add_url_rule('/', view_func=update_ingredient, methods=PUT)


ingredient = IngredientServiceBuilder.build()
