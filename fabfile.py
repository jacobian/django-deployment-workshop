"""
The tutorial's fabfile.

This starts out pretty simple -- just automating deployment on a single
server with a few commands. Then it gets a bit more complex (a basic
provisioning example).
"""

import contextlib
from fabric.api import env, run, cd, sudo, put, require, settings, hide, puts
from fabric.contrib import project, files

# This is a bit more complicated than needed because I'm using Vagrant
# for the examples.
env.hosts = ['pycon-web2', 'pycon-web1']
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
    sudo("%(root)s/bin/pip install -r %(root)s/requirements.txt" % env)
        
def reload():
    "Reload Apache to pick up new code changes."
    sudo("invoke-rc.d apache2 reload")

#
# OK, simple stuff done. Here's a more complex example: provisioning
# a server the simplistic way.
#

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


def run_chef():
    """
    Run Chef-solo on the remote server
    """
    project.rsync_project(local_dir='chef', remote_dir='/tmp', delete=True)
    sudo('rsync -ar --delete /tmp/chef/ /etc/chef/')
    sudo('chef-solo')
    
    
    
    