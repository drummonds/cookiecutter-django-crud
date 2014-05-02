from django.contrib import admin
from {{ cookiecutter.app_name }}.models import {{ cookiecutter.model_name }}

admin.site.register({{ cookiecutter.model_name }})

