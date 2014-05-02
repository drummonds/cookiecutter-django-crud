Cookiecutter Django CRUD
=====================

A cookiecutter template to create a Django app within an existing Django project, with boilerplate including:
    * A barebones Django model.
    * Django CRUD views and templates using django-vanilla-views.
    * A Django ModelForm using crispyforms.
    * Tests for all of the views using WebTest.
    * Model Mommy generated models for the tests.

Blog post walkthrough at http://wildfish.com/blog/2013/09/25/generating-django-crud-scaffolding-cookiecutter/

Quickstart
==========

1. Install cookiecutter, and apps listed in requirements.txt for our generated app.  Install them all with:

.. code-block:: console

    pip install -r https://raw.githubusercontent.com/flxfxp/cookiecutter-django-crud/master/requirements.txt


2. Run cookiecutter using this template.  Note that **it will overwrite existing files without warning if you already have an app dir of the same name**, so make sure your code is checked in or backed up.

.. code-block:: console

    cookiecutter https://github.com/flxfxp/cookiecutter-django-crud.git


3. You'll need to add floppyforms to your INSTALLED_APPS, along with your new app of course:

.. code-block:: python

    INSTALLED_APPS = (
        ..
        'crispy_forms',
        'yourproject.yourapp',
    )

4. And don't forget to hook up your urls.py:

.. code-block:: python

    url(r'^things/', include('yourproject.yourapp.urls')),


5. Run your newly created tests:

.. code-block:: console

    python manage.py test yourproject.yourapp


Feel free to fork and make it your own, or send anything back up which you think may be generally useful.
