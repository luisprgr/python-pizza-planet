from app.common.http_methods import GET
from flask import jsonify

from ..controllers import IndexController

from .service_builder import ServiceBuilder


class IndexServiceBuilder(ServiceBuilder):
    controller = IndexController
    name = 'index'
    import_name = __name__

    @classmethod
    def build_get_index_method(cls):
        def get_index():
            is_database_up, error = IndexController.test_connection()
            return jsonify(
                {
                    'version': '0.0.2',
                    'status': 'up' if is_database_up else 'down',
                    'error': error,
                }
            )

        cls.result.add_url_rule('/', view_func=get_index, methods=GET)

    @classmethod
    def build(cls):
        cls.build_blueprint()
        cls.build_get_index_method()
        return cls.result


index = IndexServiceBuilder.build()
