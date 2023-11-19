import sys
from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'PLAUTH', None)

DEFAULTS = {
    
}
