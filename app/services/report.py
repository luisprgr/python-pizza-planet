from app.common.http_methods import GET
from flask import Blueprint

from ..controllers import ReportController
from app.services.service_decorator import service

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
@service
def get_report():
    return ReportController.get_report()
