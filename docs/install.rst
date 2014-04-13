Working Environment
===================

#. Install python
#. Install pip::

    $ sudo easy_install pip

#. Install virtualenvwrapper::

    $ sudo pip install virtualenvwrapper
    $ source /usr/local/bin/virtualenvwrapper.sh

#. Create your virtualenv::

    $ mkvirtualenv hackaway

#. Install Django into the virtualenv::

    $ pip install django

Creating your Project
=====================

To create a new Django project called '**hackaway**' using django-omakase, run the following command::

    $ django-admin.py startproject --template=https://github.com/team-stroller/django-omakase/zipball/master --extension=py,rst,html --name=Procfile hackaway

Setup Development Environment
==============================

Install the project's local dependencies::

    $ pip install -r requirements/local.txt

Install postgres. Create a DB and a superuser. The database's name, username, and password must all be the project name (hackaway)::

    $ createdb hackaway
    $ createuser -P
    $ python hackaway/manage.py syncdb
    $ python hackaway/manage.py migrate djcelery

Install foreman. Run your development server::

    $ foreman start

Setup Production on Heroku
==========================

You will need the `Heroku Toolbelt`_ installed. You can use this to create your Heroku app::

    $ heroku create

.. _Heroku Toolbelt: https://toolbelt.heroku.com/

Environment Variables
---------------------

The `DJANGO_SETTINGS_MODULE` environment variable must be set to `hackaway.settings.production`. The `SECRET_KEY` environment variable must be set to a secure string::

   $ heroku config:set DJANGO_SETTINGS_MODULE=hackaway.settings.production SECRET_KEY=mysupersecretkey -r heroku

Settings
--------

You need to set the `ALLOWED_HOSTS` setting in `production.py`. This should be the domain names of your production server::

   ALLOWED_HOSTS = ['eathackaway.com']

Addons
------

You need the Redis Cloud addon or the `REDISCLOUD_URL` variable set. This is used by celery::

    $ heroku addons:add rediscloud

Acknowledgements
================

The project was created with django-omakase

.. _django-omakase: https://github.com/team-stroller/django-omakase
