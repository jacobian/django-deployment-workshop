"""
The tutorial's first fabfile: automate deployment onto a single server.

If you have Fabric installed system-wide, run with::

    fab -f single-server.py <command>

The buildout in ``fumblerooski-site`` has Fabric, too, so you can::

    fumblerooski-site/bin/fab -f ../fabfiles/single-server.py <command>
"""

from __future__ import with_statement

import os
from fabric.api import *

# I have entres in /etc/hosts which make these names work. 
# If I didn't, I'd just use IP addresses.
env.hosts = ['pycon-web1']
env.user = 'root'

env.code_root = "/home/web/django-deployment-workshop"
env.buildout_root = os.path.join(env.code_root, "fumblerooski-site")

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
    
def deploy():
    "Full deploy: push, buildout, and reload."
    push()
    buildout()
    reload()