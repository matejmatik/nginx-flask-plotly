from flask import Flask
from jinja_partials import register_extensions as jinja_partials_register_extensions
from .api import api_blueprints, register_api_error_handlers, register_dash_blueprints
from .config import FlaskConfiguration
from .utils import CustomRequest


def __setup_flask_extensions(app: Flask) -> None: ...
def __setup_docs_routing(app: Flask) -> None: ...


def initialize_flask_application() -> Flask:

    def __page_not_found(e) -> str: ...

    def __page_forbidden(e) -> str: ...

    def __page_internal_server_error(e) -> str: ...

    def __page_unauthorized(e) -> str: ...

    # Initialize the Flask application
    app = Flask(__name__, instance_relative_config=True)

    # Load the configuration
    with app.app_context():
        app.config.from_object(FlaskConfiguration)
        jinja_partials_register_extensions(app)
        register_dash_blueprints(app)
        app.register_blueprint(api_blueprints, url_prefix="/")
        __setup_flask_extensions(app)
        __setup_docs_routing(app)
        register_api_error_handlers(app)

        @app.context_processor
        def __inject_version() -> dict:
            return dict(version=FlaskConfiguration.VERSION)

    return app


app = initialize_flask_application()
app.request_class = CustomRequest
