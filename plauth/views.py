import logging
from django.utils.module_loading import import_string
from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Token
from .settings import api_settings


logger = logging.getLogger(__name__)


class BaseObtainToken(APIView):
    success_msg = "Token has been sent successfuly!"
    failed_msg = "Unable to send a token, please try again!"
    
    response_payload = {}
    
    @property
    def serializer_class(self):
        raise NotImplementedError
    
    @property
    def alias_type(self):
        raise NotImplementedError
    
    @property
    def token_type(self):
        raise NotImplementedError
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            # Validation
            user = serializer.validated_data['user']
            # Here we will initialize and send token to user
            
        else:
            return Response("Something went wrong", status=status.HTTP_400_BAD_REQUEST)