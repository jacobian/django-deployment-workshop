"""
The tutorial's first fabfile: automate deployment onto a single server.
"""

import os
from fabric.api import *

# This is a bit more complicated than needed because I'm using Vagrant
# for the examples.
env.hosts = ['pycon-web1']
env.user = 'vagrant'
env.key_filename = '/Library/Ruby/Gems/1.8/gems/vagrant-0.7.2/keys/vagrant'

# Constants for where everything lives on the server.
env.root = "/home/web/myblog"

def deploy():
    "Full deploy: push, buildout, and reload."
    push()
    update_dependencies()
    reload()
    
def push():
    "Push out new code to the server."
    with cd("%(root)s/django-mingus" % env):
        sudo("git pull")
        
    put("mingus-config/local_settings.py",
        "%(root)s/django-mingus/mingus/local_settings.py" % env,
        use_sudo=True)
    put("mingus-config/mingus.wsgi", "%(root)s/mingus.wsgi" % env, use_sudo=True)
        
def update_dependencies():
    "Update Mingus' requirements remotely."
    put("mingus-config/requirements.txt", "%s/requirements.txt", use_sudo=True)
    sudo("%(root)s/bin/pip install -r %(rot)s/requirements.txt" % env)
        
def reload():
    "Reload Apache to pick up new code changes."
    sudo("invoke-rc.d apache2 reload")

def setup():
    """
    Set up (bootstrap) a new server.
    
    This essentially does all the tasks in the script done by hand in one
    fell swoop. In the real world this might not be the best way of doing
    this -- consider, for example, what the various creation of directories,
    git repos, etc. will do if those things already exist. However, it's
    a useful example of a more complex Fabric operation.
    """
    # Initial setup and package install.
    sudo("mkdir -p /home/web/static")
    sudo("aptitude update")
    sudo("aptitude -y install git-core python-dev python-setuptools "
                              "postgresql-dev postgresql-client build-essential "
                              "libpq-dev subversion mercurial apache2 "
                              "libapache2-mod-wsgi")

    # Create the virtualenv.
    sudo("easy_install virtualenv")
    sudo("virtualenv /home/web/myblog")
    sudo("/home/web/myblog/bin/pip install -U pip")

    # Check out Mingus
    with cd("/home/web/myblog"):
        sudo("git clone git://github.com/montylounge/django-mingus.git")

    # Set up Apache
    with cd("/home/web/"):
        sudo("git clone git://github.com/jacobian/django-deployment-workshop.git")
    with cd("/etc/apache2"):
        sudo("rm -rf apache2.conf conf.d/ httpd.conf magic mods-* sites-* ports.conf")
        sudo("ln -s /home/web/django-deployment-workshop/apache/apache2.conf .")
        sudo("ln -s /home/web/django-deployment-workshop/mingus-config/mingus.wsgi /home/web/myblog/mingus.wsgi")
        sudo("mkdir -m777 -p /var/www/.python-eggs")
        
    # Now do the normal deploy.
    deploy()
    
    