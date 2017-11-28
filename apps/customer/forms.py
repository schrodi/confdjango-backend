import apps.customer.models

from django.forms import ModelForm



class CustomerForm(ModelForm):
    class Meta:
         model = apps.customer.models.Customer
         fields = '__all__'