import os

from assessme.settings.base import *
from dotenv import load_dotenv

load_dotenv()

# since it's running on my machine, show me the errors
DEBUG = True

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
# SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

SECRET_KEY = "d$pxg6fisc4iwzk&vz^s_d0lkf&k63l5a8f!obktw!jg#4zvp3"

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# show mail messages on the terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
