from django.http import Http404
from django_remote_forms.forms import RemoteForm

from rest_framework import status , generics , mixins, permissions, views
from rest_framework.response import Response

from django.contrib.auth.models import Permission
from  . import serializers

class UserPermissionList(generics.ListCreateAPIView):
    
    """
    lists all permissions of the requesting user

    * Requires token authentication.
    * Only logged in users are able to access this view
    """
    
    queryset = Permission.objects
    serializer_class = serializers.PermissionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`

        if request.user.is_superuser:
            permissions = self.get_queryset().all()
        else:
            permissions = request.user.user_permissions.all() | self.get_queryset().filter(group__user=request.user)

        
        
        
        serializer = serializers.PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

"""
class UserPermissionList(views.APIView):
    
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Permission.objects.all()
    
    def get_object(self, request, format=None):
        try:
            print request.user
            
            if request.user.is_superuser:
                return Permission.objects.all()
            return user.user_permissions.all() | Permission.objects.filter(group__user=user)
                
        except apps.customer.models.Customer.DoesNotExist:
            
            raise Http404

"""

class PermissionList(generics.ListCreateAPIView):
    def get_object(self, pk):
        try:
          
            def get_user_permissions(user):
                if user.is_superuser:
                    return Permission.objects.all()
                return user.user_permissions.all() | Permission.objects.filter(group__user=user)
                
        except apps.customer.models.Customer.DoesNotExist:
            
            raise Http404
    

