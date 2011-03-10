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

def push():
    "Push out new code to the server."
    with cd("%(root)s/django-mingus" % env):
        sudo("git pull")
        
    put("mingus-config/web1.py",
        "%(root)s/django-mingus/mingus/settings.py" % env,
        use_sudo=True)
    put("mingus-config/mingus.wsgi", "%(root)s/mingus.wsgi" % env, use_sudo=True)
        
def update_dependencies():
    "Update Mingus' requirements remotely."
    put("mingus-config/requirements.txt", "%s/requirements.txt", use_sudo=True)
    sudo("%(root)s/bin/pip install -r %(rot)s/requirements.txt" % env)
        
def reload():
    "Reload Apache to pick up new code changes."
    sudo("invoke-rc.d apache2 reload")
    
def deploy():
    "Full deploy: push, buildout, and reload."
    push()
    update_dependencies()
    reload()