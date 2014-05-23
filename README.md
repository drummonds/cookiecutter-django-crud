Cookiecutter Django CRUD
=====================

A cookiecutter *template* to create a Django app within an existing Django project, with boilerplate including:

* A barebones Django model.
* Django CRUD views and templates using django-vanilla-views.
* A Django ModelForm using crispyforms.
* Tests for all of the views using WebTest.
* Model Mommy generated models for the tests.

This is not the cookiecutter application which is here https://pypi.python.org/pypi/cookiecutter.

Quickstart
==========

Install cookiecutter (the application), and apps listed in requirements.txt for our generated app.  Install them all with:

    pip install -r https://raw.githubusercontent.com/drummonds/cookiecutter-django-crud/master/requirements.txt


Run cookiecutter using this template.  Note that **it will overwrite existing files without warning if you already have an app dir of the same name**, so make sure your code is checked in or backed up.

    cookiecutter https://github.com/drummonds/cookiecutter-django-crud.git

I installed cookie cutter by hand to `~/project/cookiecutter-django-crud` so the next time I ran it I used the following command rather than getting it again

You'll need to add crispy forms to your settings file, along with your new app of course and a link for the 
template pack for bootstrap3:
    
````
CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS += (
    'crispy_forms',
    'yourproject.stocks',
    )
````

And don't forget to hook up your urls.py (assuming you have your apps at the same level as the application):

    url(r'^things/', include('yourapp.urls')),

Update your database which is (follow instructions if using South for migrations):
````
python manage.py syncdb --settings=myproj.settings.local
python manage.py schemamigration things --initial --settings=myproj.settings.local
python manage.py migrate things --initial --settings=myproj.settings.local
````
(Note the settings file will depend on what you are doing in your project.)

Run your newly created tests:

    python manage.py test yourproject.yourapp


Then at `http://127.0.0.1/things/` you should see a list with basic CRUD controls.

Happy start. 
