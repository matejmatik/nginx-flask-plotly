from os import getenv


class FlaskConfiguration:
    # General Config
    APP_NAME = getenv("PROJECT_NAME", "Flask API")
    VERSION = getenv("PROJECT_VERSION", "0.0.0")
    DEBUG = True

    STATIC_FOLDER = getenv("STATIC_FOLDER", "static")
    TEMPLATE_FOLDER = getenv("TEMPLATE_FOLDER", "templates")

    SECRET_KEY = getenv("SECRET_KEY")
    WTF_CSRF_ENABLED = getenv("WTF_CSRF_ENABLED", True)
    WTF_CSRF_SECRET_KEY = getenv("WTF_CSRF_SECRET_KEY")

    RECAPTCHA_PUBLIC_KEY = getenv("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = getenv("RECAPTCHA_PRIVATE_KEY")
