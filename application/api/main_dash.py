from .dash_apps import default_dash_app


def register_dash_blueprints(app):

    app = default_dash_app.initialize_dash_app(
        server=app,
        path="/default-dash-app/",
        title="Default Dash App",
    )
