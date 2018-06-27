import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@bf3^740bjyrgh#77)i8cy(!*dqm6u(osr2#3!b-&czg3vu2_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'mail.climatim.ru'

# Port for sending e-mail.
EMAIL_PORT = 587

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'info@climatim.ru'
EMAIL_HOST_PASSWORD = 'climatim-mlimatim123'
EMAIL_USE_TLS = True