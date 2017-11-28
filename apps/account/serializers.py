from rest_framework import serializers
from django.contrib.auth.models import Permission
from rest_framework.fields import CurrentUserDefault


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'
        

