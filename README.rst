Django Deployment Workshop
==========================

This is code and configuration for my Django Deployment Workshop.

Here you'll find example config used to set up an example deployment
environment for a Python WSGI stack, including:

* A Django site deployed with Pip_, Virtualenv_, and Fabric_.
* Apache/mod_wsgi_ and Gunicorn_ application servers.
* Nginx_ load balancers and media servers.
* Memcached_.
* PostgreSQL_ with `pgpool`_

.. _pip: http://pip.rtfd.org/
.. _virtualenv: http://virtualenv.rtfd.org/
.. _fabric: http://fabfile.org/
.. _buildout: http://buildout.org/
.. _mod_wsgi: http://modwsgi.org/
.. _nginx: http://wiki.nginx.org/
.. _memcached: http://memcached.org/
.. _postgresql: http://postgresql.org/
.. _pgpool: http://pgpool.projects.postgresql.org/
.. _gunicorn: http://gunicorn.org/

I've made comments and notes where possible, but it's entirely possible that
this won't make a whole lot of sense without actually taking the class. But
this is all BSD-licensed, so please feel free to use it as a starting point
for you own deployments.

The Django site used for the examples is Kevin Fricovsky's Mingus_, a blog
application built on a bunch existing reusable apps.

.. _mingus: https://github.com/montylounge/django-mingus

Getting the app running
=======================

See Mingus's INSTALL_ doc for the basics of getting Mingus running. If you're
on a VM or remote server remember that you'll have to ``runserver 0.0.0.0:8000`` to get Django listening on public IP interfaces.

.. _install: https://github.com/montylounge/django-mingus/blob/master/docs/INSTALL.textile

After than, start deploying. My script for the install is in ``notes``; be sure to follow along with the most recent one (PyCon 2011 as of this writing).
The other scripts are there for posterity.

If you're not using Ubuntu 10.04 LTS then YMMV.

Further reading
===============

By my count this three-hour class covers about a dozen different pieces of
technology. Below are some links to documentation of these various bits. If
you read through all of it until you understand every command and
configuration option I've used, you'll be well on your way towards groking
this stuff. Good luck!

    * Ubuntu_.
    * git_ (also see the `git book`_).
    * Pip_.
    * Virtualenv_.
    * Django_; see particularly the `settings reference`_.
    * Apache_; the `directive quick reference`_ is especially useful.
    * mod_wsgi_:
        * `Django's mod_wsgi docs`_.
        * `mod_wsgi's Django docs`_.
    * Gunicorn_
    * `PostgreSQL docs`_, including:
        * `Server configuration`_ (``postgresql.conf``).
        * `Client authentication`_ (``pg_hba.conf``).
    * Fabric_.
    * Nginx_, specifically the upstream_ and proxy_ modules.
    * memcached_.
    * Django's `caching framework`_.
    * pgpool2_.
    * Chef_, specifically `Chef Solo`_.
    
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
.. _chef: http://wiki.opscode.com/display/chef/Home
.. _chef solo: http://wiki.opscode.com/display/chef/Chef+Solo