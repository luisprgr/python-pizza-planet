from ..controllers import BeverageController
from .service_builder import ServiceBuilder


class BeverageServiceBuilder(ServiceBuilder):
    controller = BeverageController
    name = 'beverage'
    import_name = __name__


beverage = BeverageServiceBuilder.build()
