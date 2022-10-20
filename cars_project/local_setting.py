# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-db97#3_y26%9+^%m*xve+@!*6x^gqdvu7!a1c-8wl-%%l&vcuz'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password99!',

    }
}