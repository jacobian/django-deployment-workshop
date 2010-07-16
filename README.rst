Django Deployment Workshop
==========================

This is code and configuration for my Django Deployment Workshop at PyCon
2010, OSCON 2010, and beyond.

Here you'll find example config used to set up an example deployment environment
for a Python WSGI stack, including:

* A Django site deployed with Fabric_ and Buildout_
* Apache/mod_wsgi_ application servers
* Nginx_ load balancers and media servers
* Memcached_
* PostgreSQL_ with `pg_standby`_

.. _fabric: http://fabfile.org/
.. _buildout: http://buildout.org/
.. _mod_wsgi: http://modwsgi.org/
.. _nginx: http://wiki.nginx.org/
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

Getting the app running
=======================

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

   (You could also use the server's public IP explicitly.)

What's next
===========

After than, start deploying. My notes, the ones I use when I teach the class,
are available here. If you're not using Ubuntu 10.04 LTS then YMMV.

Further reading
===============

By my count this three-hour class covers about a dozen different pieces of
technology. Below are some links to documentation of these various bits. If
you read through all of it until you understand every command and
configuration option I've used, you'll be well on your way towards groking
this stuff. Good luck!

    * Ubuntu_
    * git_ (also see the `git book`_)
    * Buildout_
    * Django_; see particularly the `settings reference`_
    * Apache_; the `directive quick reference`_ is especially useful
    * mod_wsgi_
        * `Django's mod_wsgi docs`_
        * `mod_wsgi's Django docs`_
    * `PostgreSQL docs`_, including:
        * `Server configuration`_ (``postgresql.conf``)
        * `Client authentication`_ (``pg_hba.conf``)
    * Fabric_
    * Nginx_, specifically the upstream_ and proxy_ modules
    * memcached_
    * Django's `caching framework`_
    * pgpool2_
    * pg_standby_
    
.. _ubuntu:
.. _git: http://git-scm.com/documentation
.. _`git book`: http://book.git-scm.com/
.. _django: http://docs.djangoproject.com/en/dev/
.. _`settings reference`: http://docs.djangoproject.com/en/dev/ref/settings/
.. _apache: http://httpd.apache.org/docs/2.2/
.. _`directive quick reference`: http://httpd.apache.org/docs/2.2/mod/quickreference.html
.. _`django's mod_wsgi docs`: http://docs.djangoproject.com/en/dev/howto/deployment/modwsgi/
.. _`mod_wsgi's Django docs`: http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango
.. _`postgresql docs`: http://www.postgresql.org/docs/current/static/
.. _`server configuration`: http://www.postgresql.org/docs/8.4/static/runtime-config.html
.. _`client authentication`: http://www.postgresql.org/docs/8.4/static/client-authentication.html
.. _upstream: http://wiki.nginx.org/NginxHttpUpstreamModule
.. _proxy: http://wiki.nginx.org/NginxHttpProxyModule
.. _`caching framework`: http://docs.djangoproject.com/en/dev/topics/cache/
.. _pgpool2: http://pgpool.projects.postgresql.org/pgpool-II/doc/pgpool-en.html