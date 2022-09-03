from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import ReportManager

class ReportController:
    manager = ReportManager

    @classmethod
    def get_report(cls):
        pass
