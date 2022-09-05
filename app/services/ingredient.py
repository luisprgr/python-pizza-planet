from ..controllers import IngredientController
from .service_builder import ServiceBuilder


class IngredientServiceBuilder(ServiceBuilder):
    controller = IngredientController
    name = 'ingredient'
    import_name = __name__


ingredient = IngredientServiceBuilder.build()
