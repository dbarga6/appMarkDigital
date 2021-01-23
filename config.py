from os import environ


class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('DATABASE_USER', 'gentxxxxelella'),
        environ.get('DATABASE_PASSWORD', 'xxxxx'),
        environ.get('DATABASE_HOST', 'dxxb'),
        environ.get('DATABASE_PORT', 5432),
        environ.get('DATABASE_NAME', 'xxxx')
    )


class DesaConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Desa': DesaConfig
}
