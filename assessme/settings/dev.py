from dotenv import load_dotenv

from assessme.settings.base import *

load_dotenv()

# since it's running on my machine, show me the errors
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

SECRET_KEY = "d$pxg6fisc4iwzk&vz^s_d0lkf&k63l5a8f!obktw!jg#4zvp3"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# show mail messages on the terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
