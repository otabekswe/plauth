from random import randint

from django.utils import timezone
from django.core.mail import send_mail


from .settings import api_settings


def generate_token() -> str:
    '''
    Effortlessly generate 6-digit strings with or without leading zeros for versatile applications.
    '''
    return str("%06d" % randint(0, 999999))


def token_validator(token: str) -> bool:
    '''
    Validate a token to ensure it is length's 6 and contains only digits.
    '''
    return token.isdigit() and len(token) == 6


def token_age_validator(token: str) -> bool:
    '''
    Validate a token to ensure it is less than TOKEN_EXPIRATION_TIME in settings.
    '''
    seconds = (timezone.now() - token.created_at).total_seconds()
    expery_time = api_settings.TOKEN_EXPIRATION_TIME * 60
    
    if seconds >= expery_time:
        token.is_active = False
        token.save()
        return False
    
    return True
    

def send_via_email(user, token):
    '''
    Send a token via email to the user. It allwos you to customize the email message, subject and sender.
    '''
    try:
        if api_settings.EMAIL_SENDER:
            # Replace the token in the HTML message if it exists
            html_message = api_settings.EMAIL_HTML_MESSAGE.replace('<TOKEN>', token.key)
            
            # Replace the token in the plaintext message if it exists
            api_settings.EMAIL_PLAINTEXT_MESSAGE = api_settings.EMAIL_PLAINTEXT_MESSAGE.replace('<TOKEN>', token.key)
            
            # Send the email
            send_mail(
                api_settings.EMAIL_SUBJECT,
                api_settings.EMAIL_PLAINTEXT_MESSAGE,
                api_settings.EMAIL_SENDER,
                [user.email],
                fail_silently=False,
                html_message=api_settings.EMAIL_HTML_MESSAGE
            )
        else:
            # Logging message will be here
            return False
        return True
    except Exception as e:
        # Logging message will be here
        return False


def send_via_telegram_bot(user, token):
    '''
    Send a token via telegram bot to the user.
    '''
    pass


def send_via_sms(user, token):
    '''
    Send a token via SMS to the user.
    '''
    pass