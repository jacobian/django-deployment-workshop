"""
The tutorial's first fabfile: automate deployment onto a single server.

Run with::

    fab -f fabfiles/single-server.py <command>
    
Expects to be run from the parent directory.
"""

import os
from fabric.api import *

# I have entries in /etc/hosts which make these names work. 
# If I didn't, I'd just use IP addresses.
env.hosts = ['pyweb-web1']
env.user = 'root'

# Constants for where everything lives on the server.
env.root = "/home/web/myblog"

def push():
    "Push out new code to the server."
    with cd(env.code_root):
        run("git pull")
        put("mingus-config/web1.py", "%(root)s/django-mingus/mingus/settings.py" % env)
        put("mingus-config/mingus.wsgi", "%(root)s/mingus.wsgi" % env)
        
def update_dependencies():
    "Update Mingus' requirements remotely."
    put("mingus-config/requirements.txt", "%s/requirements.txt")
    run("%(root)s/bin/pip install -r %(rot)s/requirements.txt" % env)
        
def reload():
    "Reload Apache to pick up new code changes."
    run("invoke-rc.d apache2 reload")
    
def deploy():
    "Full deploy: push, buildout, and reload."
    push()
    buildout()
    reload()