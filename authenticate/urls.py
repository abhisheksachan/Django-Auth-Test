"""urls for authenticate view."""
from django.conf.urls import url

urlpatterns = [
    url(r'login/', 'authenticate.views.login_view', name='login_view'),
    url(r'logout/', 'authenticate.views.logout_view', name='logout_view'),
    url(r'test/', 'authenticate.views.simple_view', name='simple_view'),

]
