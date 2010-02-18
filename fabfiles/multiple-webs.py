"""
The tutorial's second fabfile: automate deployment onto multiple web servers.

See ``single-server.py`` for notes on how to run these fabfiles, and for more
comments.
"""

from __future__ import with_statement

import os
from fabric.api import *
from fabric.contrib import files

env.hosts = ['pycon-web1', 'pycon-web2']
env.user = 'root'
env.web_root = "/home/web"
env.code_root = os.path.join(env.web_root, "django-deployment-workshop")
env.buildout_root = os.path.join(env.code_root, "fumblerooski-site")

def setup():
    "Set up and bootstrap a new web server."
    
    # Install needed packages
    run('aptitude -y install git-core python-dev postgresql-dev postgresql-client build-essential libpq-dev apache2 libapache2-mod-wsgi')

    # Make the code directories, and go get the code
    run('mkdir -p %s' % os.path.join(env.web_root, "static"))
    with cd(env.web_root):
        run('git clone git://github.com/jacobian/django-deployment-workshop.git')

    # Bootstrap and buildout
    with cd(env.buildout_root):
        run('python bootstrap.py')
        run('./bin/buildout')
        
        # In the real world, the settings file would already contain the correct
        # DATABASE_HOST. Since this is a demo, we'll do something somewhat
        # hackish -- but cool -- and swap in the correct DATABASE_HOST at
        # bootstrap time.
        dbip = prompt("What's the private IP for DB1?")
        files.sed(os.path.join(env.buildout_root, "fski", "settings.py"),
                  before = r"^DATABASE_HOST.*$",
                  after  = r'DATABASE_HOST = "%s"' % dbip.strip())
    
    # Install the Apache conf
    with cd("/etc/apache2"):
        run('rm -rf apache2.conf conf.d/ httpd.conf magic mods-* sites-* ports.conf ')
        run('ln -s /home/web/django-deployment-workshop/apache/apache2.conf .')

    # Make the Python eggs directory.
    run('mkdir -m777 -p /var/www/.python-eggs')
    
    # Done - where! Now restart Apache.
    run('invoke-rc.d apache2 restart')

def trysed():
    dbip = '10.177.58.115'

def push():
    "Push out new code to the server."
    with cd(env.code_root):
        run("git pull")
        
def buildout():
    "Run the buildout remotely."
    with cd(env.buildout_root):
        run("./bin/buildout")
        
def reload():
    "Reload Apache to pick up new code changes."
    run("invoke-rc.d apache2 reload")

def flush_cache():
    "Flush memcached."
    run("invoke-rc.d memcached restart")

def deploy():
    "Full deploy: push, buildout, and reload."
    push()
    buildout()
    reload()
    flush_cache()