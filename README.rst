Django Deployment Workshop
==========================

This is code and configuration for my Django Deployment Workshop at PyCon 2010
(and beyond).

Here you'll find example config used to set up an example deployment environment
for a Python WSGI stack, including:

* A Django site deployed with Fabric_ and Buildout_.
* Apache/mod_wsgi_ application servers.
* Nginx_ load balancers and media servers.
* Memcached_.
* PostgreSQL_ with `pg_standby`_

.. _fabric: http://fabfile.org/
.. _buildout: http://buildout.org/
.. _mod_wsgi: http://modwsgi.org/
.. _nginx: http://nginx.net/
.. _memcached: http://memcached.org/
.. _postgresql: http://postgresql.org/
.. _pg_standby: http://www.postgresql.org/docs/current/static/pgstandby.html

I've made comments and notes where possible, but it's entirely possible that
this won't make a whole lot of sense without actually taking the class. But this
is all BSD-licensed, so please feel free to use it as a starting point for you
own deployments.

The Django site used for the examples is Derek Willis' Fumblerooski_. Many
thanks to Derek for letting me (ab)use his code!

.. _fumblerooski: http://github.com/dwillis/fumblerooski

Getting started
===============

1. Grab the dump file. This file isn't for public distribution, so it's not
   linked here. If you're in one of my classes you'll get the link in an email.

2. Make sure you have PostgreSQL installed or have access to a database. For
   easiest use, you'll want a db named ``fumblerooski``, owned by a user of the
   same name, and you'll want to have configured PostgreSQL to allow
   non-authenticated access. (Otherwise, you'll need to edit
   ``fski/settings.py`` with the appropriate credentials.)

3. Restore the data into the database::

        zcat fumblerooski-dump.sql.gz | psql fumblerooski 
    
   You'll probably get a bunch of warnings and errors, but it should complete
   successfully anyway.

4. Run the Buildout::

        python bootstrap.py
        ./bin/buildout
    
5. You can verify that you've got the basics of everything working okay by
   running the dev. server::

        ./bin/django runserver
    
   If you're running this on a VM and want to be able to access the site remotely,
   make sure to make the dev. server listen publicly::
   
        ./bin/django runserver 0.0.0.0:8000
        
