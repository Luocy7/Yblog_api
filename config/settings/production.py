from .common import *  # noqa
from .common import env

env_file = str(BASE_DIR / 'envs' / 'production' / '.django')
env.read_env(env_file)

SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
DEBUG = False

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db()}  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

# CACHES
# ------------------------------------------------------------------------------
# https://django-redis-cache.readthedocs.io/en/latest/
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            'DB': 1,
        },
    }
}

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
