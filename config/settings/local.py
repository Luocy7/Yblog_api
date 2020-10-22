from .common import *  # noqa
from .common import env

env_file = str(BASE_DIR / 'envs' / 'local' / '.django')
env.read_env(env_file)

DEBUG = True
SECRET_KEY = "fake-secret-key-for-development"
ALLOWED_HOSTS = ["*"]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "localhost"]
if env("USE_DOCKER", default=False):
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

YBLOG_DOMAIN = env.str("YBLOG_DOMAIN", default="http://127.0.0.1:8000")

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js",
}

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa
INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db(),
}

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": "backups"}
# CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://redis:6379/0")

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
