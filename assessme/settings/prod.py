from dotenv import load_dotenv
import dj_database_url

from assessme.settings.base import *

load_dotenv()

# since it's running on my machine, show me the errors
DEBUG = False

# once heroku fixes automatic deployment, we can use this
# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")

ALLOWED_HOSTS = ["assessme-project.herokuapp.com"]

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)

django_heroku.settings(locals())
del DATABASES["default"]["OPTIONS"]["sslmode"]

SECRET_KEY = os.getenv("SECRET_KEY")

# show mail messages on the terminal
EMAIL_BACKEND = os.getenv("EMAIL_HOST_USER")
