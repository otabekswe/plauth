import uuid
from django.db import models
from django.conf import settings

from .utils import generate_token

# Create your models here.
class TokenManager(models.Manager):
    def active(self) -> bool:
        return self.get_queryset().filter(is_active=True)
    
    def inactive(self) -> bool:
        return self.get_queryset().filter(is_active=False)


class BaseToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=None)
    is_active = models.BooleanField(default=True)
    to_alias = models.CharField(max_length=250, blank=True)
    to_alias_type = models.CharField(max_length=20, blank=True)
    
    objects = TokenManager()
    
    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return str(self.key)


class Token(BaseToken):
    TOKEN_TYPE_AUTH = 'AUTH'
    TOKEN_TYPE_VERIFY = 'VERIFY'
    TOKEN_TYPES = ((TOKEN_TYPE_AUTH, 'Auth'), (TOKEN_TYPE_VERIFY, 'Verify'))
    
    key = models.CharField(max_length=6, default=generate_token)
    type = models.CharField(max_length=20, choices=TOKEN_TYPES)
    
    class Meta(BaseToken.Meta):
        verbose_name = 'Token'