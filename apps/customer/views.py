import apps.customer.models
import apps.customer.serializers
import apps.customer.forms

from django.http import Http404
from django_remote_forms.forms import RemoteForm

from rest_framework import status , generics , mixins, permissions, views



from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class API_List(generics.ListCreateAPIView):

    queryset = apps.customer.models.Customer.objects.all()
    serializer_class = apps.customer.serializers.CustomerSerializer

    #authentication_classes = [SessionAuthentication]
    permission_classes = [ permissions.DjangoModelPermissions]

    def get(self, request):

        c = super(API_List, self).get(request)
  
        return c

class API_Detail(views.APIView):
    def get_object(self, pk):
        try:
           return apps.customer.models.Customer.objects.get(pk=pk)
        except apps.customer.models.Customer.DoesNotExist:
            raise Http404


class API_CustomerForm(views.APIView):
    def get_object(self):
        form = apps.customer.forms.CustomerForm
        
        
        

form = apps.customer.forms.CustomerForm()
remote_form = RemoteForm(form)
remote_form_dict = remote_form.as_dict()
#print remote_form_dict