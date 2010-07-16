"""
This is my private fabfile I use to automate parts of the teaching of the
class. It doesn't really serve any pedagogical purpose; see the fabiles in
``fabfiles/`` for better examples.
"""

import os
import cloudservers
from fabric.api import *
from fabric.contrib import files
from unipath import FSPath as Path

CS = cloudservers.CloudServers(os.environ['CLOUD_SERVERS_USERNAME'],
                               os.environ['CLOUD_SERVERS_API_KEY'])

env.hosts = ['pycon-web1', 'pycon-web2', 'pycon-db1', 'pycon-db2']
env.user = 'root'

def bootem():
    servers = []
    flavor = CS.flavors.find(ram=256)
    image = CS.images.find(name="Ubuntu 10.04 LTS (lucid)")
    for name in env.hosts:
        server = CS.servers.create(name, flavor=flavor, image=image)
        servers.append(server)
        print "%s: ips: %s/%s pass: %s" % (name, server.public_ip, server.private_ip, server.adminPass)

def copyid():
    for name in env.hosts:
        local('ssh-copy-id %s' % name)
        
def setup():
    with hide('stdout', 'stderr'):
        run('aptitude -y install bash-completion')
        run('echo ". /etc/bash_completion" >> .bashrc')

def killem():
    for name in env.hosts:
        CS.servers.find(name=name).delete()

del Path