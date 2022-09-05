from flask_lambda import FlaskLambda
from app import register_blueprints, register_plugins, cors_app

app_lambda = FlaskLambda(__name__)
app_lambda.config.from_object('app.settings.Config')
register_blueprints(app_lambda)
register_plugins(app_lambda)
cors_app(app_lambda)
