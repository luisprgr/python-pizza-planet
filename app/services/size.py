from ..controllers import SizeController

from .service_builder import ServiceBuilder


class SizeServiceBuilder(ServiceBuilder):
    controller = SizeController
    name = 'size'
    import_name = __name__


size = SizeServiceBuilder.build()
