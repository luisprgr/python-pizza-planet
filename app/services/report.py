from app.common.http_methods import GET
from flask import jsonify

from ..controllers import ReportController
from .service_builder import ServiceBuilder


class ReportServiceBuilder(ServiceBuilder):
    controller = ReportController
    name = 'report'
    import_name = __name__

    @classmethod
    def build_get_report_method(cls):
        def get_report():
            report, error = ReportController.get_report()
            response = report if not error else {'error': error}
            status_code = 200 if not error else 400
            return jsonify(response), status_code

        cls.result.add_url_rule('/', view_func=get_report, methods=GET)

    @classmethod
    def build(cls):
        cls.build_blueprint()
        cls.build_get_report_method()
        return cls.result


report = ReportServiceBuilder.build()
