Cookiecutter Django CRUD
=====================

A cookiecutter template to create a Django app within an existing Django project, with boilerplate including:

* A barebones Django model.
* Django CRUD views and templates using django-vanilla-views.
* A Django ModelForm using crispyforms.
* Tests for all of the views using WebTest.
* Model Mommy generated models for the tests.

Quickstart
==========

Install cookiecutter, and apps listed in requirements.txt for our generated app.  Install them all with:

    pip install -r https://raw.githubusercontent.com/flxfxp/cookiecutter-django-crud/master/requirements.txt


Run cookiecutter using this template.  Note that **it will overwrite existing files without warning if you already have an app dir of the same name**, so make sure your code is checked in or backed up.

    cookiecutter https://github.com/flxfxp/cookiecutter-django-crud.git


You'll need to add floppyforms to your INSTALLED_APPS, along with your new app of course:
    
    INSTALLED_APPS = (
        ..
        'crispy_forms',
        'yourproject.yourapp',
    )

And don't forget to hook up your urls.py:

    url(r'^things/', include('yourproject.yourapp.urls')),


Run your newly created tests:

    python manage.py test yourproject.yourapp