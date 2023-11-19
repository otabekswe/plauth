import logging 
from django.db.models import signals
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import Token
from .utils import generate_token
from .settings import api_settings

User = get_user_model()


# Define signals here
@receiver(signals.post_save, sender=Token)
def invalidate_previous_token(sender, instance, created, **kwargs):
    '''
    Invalidate previous tokens when a new one is created or used.
    '''
    if isinstance(instance, Token):
        token = Token.objects.active().filter(user=instance.user)
        token.exclude(id=instance.id).update(is_active=False)
        logging.info('Token {} is now inactive.'.format(token))


@receiver(signals.pre_save, sender=Token)
def check_uniqueness(sender, instance, **kwargs):
    '''
    Ensuring Token Uniqueness: 
    Verify and regenerate if necessary. Upholding uniqueness standards for both authentication and verification tokens.
    '''
    if instance._state.adding:
        if isinstance(instance, Token):
            unique = False
            tries = 0
        
            if Token.objects.filter(key=instance.key, is_active=True).exists():
                while tries < api_settings.TOKEN_GENERATION_ATTEMPTS:
                    tries += 1
                    new_key = generate_token()
                    instance.key = new_key

                    if not Token.objects.filter(key=new_key, is_active=True).exists():
                        unique = True
                        break

                if not unique:
                    raise ValidationError('Unable to generate a unique token after {} attempts.'.format(tries))
         

