from django.conf.urls import url


from . import views


urlpatterns = [
	#url(r'^(?i)$', views.Table.as_view(), name='customer_table'),
    
	#url(r'^(?i)(?P<customer>[0-9]+)/edit/$', views.Edit.as_view(), name='customer_edit'),
    
    url(r'^account/permissions/$', views.UserPermissionList.as_view()),
    # url(r'^account/(?P<pk>[0-9]+)/$', views.API_Detail.as_view()),
    
    

]