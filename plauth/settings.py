from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'PLAUTH', None)

DEFAULTS = {
    # Allowed auth types, by default only email is allowed
    'AUTH_TYPES': 'EMAIL',
    
    # Amount of time in seconds before a token expires
    'EXPIRATION_TIME': 10 * 60,
    
    # Email
    # The email address that will be used to send the token
    'EMAIL_SENDER': None, # Email address that will be used to send the token
    'EMAIL_SUBJECT': 'Registration Code', # Subject of the email
    'EMAIL_PLAINTEXT_MESSAGE': 'Your verification code is <TOKEN>', # Plaintext message of the email
    'EMAIL_HTML_MESSAGE': 'platuh_email.html', # HTML message of the email (path to template)
    
    # For email verification
    'EMAIL_VERIFICATION_SENDER': None, # Email address that will be used to send the token
    'EMAIL_VERIFICATION_SUBJECT': 'Verification Code', # Subject of the email
    
    # Number of attempts to generate a unique token
    'TOKEN_GENERATION_ATTEMPTS': 5, 
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS, None)