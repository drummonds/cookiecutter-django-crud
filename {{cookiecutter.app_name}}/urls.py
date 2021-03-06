from django.conf.urls import patterns, url
from {{ cookiecutter.app_name }}.views import {{ cookiecutter.model_name }}List, {{ cookiecutter.model_name }}Create, {{ cookiecutter.model_name }}Detail, {{ cookiecutter.model_name }}Update, {{ cookiecutter.model_name }}Delete

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^new/$', {{ cookiecutter.model_name }}Create.as_view(), name='{{ cookiecutter.model_name|lower }}_create'),
    url(r'^(?P<pk>\d+)/$', {{ cookiecutter.model_name }}Detail.as_view(), name='{{ cookiecutter.model_name|lower }}_detail'),
    url(r'^(?P<pk>\d+)/update/$', {{ cookiecutter.model_name }}Update.as_view(), name='{{ cookiecutter.model_name|lower }}_update'),
    url(r'^(?P<pk>\d+)/delete/$', {{ cookiecutter.model_name }}Delete.as_view(), name='{{ cookiecutter.model_name|lower }}_delete'),
    url(r'^', {{ cookiecutter.model_name }}List.as_view(), name='{{ cookiecutter.model_name|lower }}_list'),
)

