from rest_framework import serializers
import apps.customer.models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.customer.models.Customer
        fields = '__all__'


