from ..controllers import OrderController
from .service_builder import ServiceBuilder


class OrderServiceBuilder(ServiceBuilder):
    controller = OrderController
    name = 'order'
    import_name = __name__

    @classmethod
    def build_update_method(cls):
        return None


order = OrderServiceBuilder.build()
