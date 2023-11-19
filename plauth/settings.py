import sys
from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'PLAUTH', None)

DEFAULTS = {
    # Number of attempts to generate a unique token
    'TOKEN_GENERATION_ATTEMPTS': 5, 
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS, None)