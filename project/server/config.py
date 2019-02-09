"""
Server configuration - based on the environments from the .env file
"""
import environs


env = environs.Env()
env.read_env()


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = env("APP_NAME", "QGIS Lightweight Plugin Server")
    FLASK_ENV = env("FLASK_ENV", "development")
    SECRET_KEY = env("SECRET_KEY", "hannah henry and marcie")

    # database
    BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", 4)
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS",
                                              False)
    SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI')

    # security
    SECURITY_PASSWORD_HASH = env("SECURITY_PASSWORD_HASH")
    SECURITY_PASSWORD_SALT = env("SECURITY_PASSWORD_SALT")
    SECURITY_TRACKABLE = env.bool("SECURITY_TRACKABLE")
    SECURITY_REGISTERABLE = env.bool("SECURITY_REGISTERABLE")
    SECURITY_SEND_REGISTER_EMAIL = env.bool("SECURITY_SEND_REGISTER_EMAIL")
    SECURITY_POST_LOGIN_VIEW = env('SECURITY_POST_LOGIN_VIEW')
    SECURITY_POST_LOGOUT_VIEW = env('SECURITY_POST_LOGOUT_VIEW')
    SECURITY_POST_REGISTER_VIEW = env('SECURITY_POST_REGISTER_VIEW')

    # other
    WTF_CSRF_ENABLED = env.bool('WTF_CSRF_ENABLED')
    MAX_CONTENT_LENGTH = env.int('MAX_CONTENT_LENGTH', 4194304)


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG_TB_ENABLED = env.bool('DEBUG_TB_ENABLED')
    DEBUG_TB_INTERCEPT_REDIRECTS = env.bool('DEBUG_TB_INTERCEPT_REDIRECTS')


class ProductionConfig(BaseConfig):
    """Production configuration."""

    pass

class TestingConfig(ProductionConfig):
    """Testing configuration."""

    TESTING = True
