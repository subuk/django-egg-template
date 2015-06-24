===================
Django-egg-template
===================

`Template <https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-startproject>`_ for packaged django projects.

Just create new projects with the following command:

::

    django-admin.py startproject --template=https://github.com/subuk/django-egg-template/archive/master.zip myproject


Usage
-----


- Create new project specific applications in src/{{ project_name }} and add it to INSTALLED_APPS as:

::

    INSTALLED_APPS = [
        ...
        '{{ project_name }}.coolapp',
        '{{ project_name }}.authentication',
        ...
    ]

- Instead of manage.py use {{ project_name }} from any directory, e.g:

::

    {{ project_name }} migrate

- Save deployment dependencies to setup.py:requires
- Save development and test dependencies to setup.py:develop_requires
- Install for development with

::

    pip install -e .[develop]

- Deploy

::

    pip install git://git@github.com/...
