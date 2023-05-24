# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My Dependencies
    # CORS Headers
    "corsheaders",
    # Django rest framework
    'rest_framework',
    'rest_framework_simplejwt',
    # My Apps
    'recipes',
    'authors',
    'tag',
]
