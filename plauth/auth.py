from django.core.exceptions import PermissionDenied

from .models import Token


def auth_by_token(token):
    try:
        token = Token.objects.active().get(key=token, is_active=True)
        
        if token != None:
            token.is_active = False
            token.save()
            
            return token.user
    except Token.DoesNotExist:
        pass
    except PermissionDenied:
        pass
    
    return None
