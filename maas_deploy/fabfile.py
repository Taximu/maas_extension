##
# Fabric module to deploy MaaS. Run as root user.
#

import logging

from fabric.api import *
from fabric.colors import cyan, green, red

logging.basicConfig(level=logging.ERROR)
para_log = logging.getLogger('paramiko.transport')
para_log.setLevel(logging.ERROR)

from fabric import Connection, task
from fabric.utils import cyan, green, red

CONTROLLER_HOST = "user@ipaddress"

@task
def install_maas(c=None):
    """Installs MaaS on a remote machine."""
    if not c:
        c = Connection(CONTROLLER_HOST)

    c.sudo('add-apt-repository ppa:maas-maintainers/stable -y')
    c.sudo('apt-get update')
    c.sudo('apt-get install -y maas maas-dhcp maas-dns')

    eth_name = input("Specify ethernet device for wakeonlan: ")
    print(cyan(f"Ethernet device set to: {eth_name}"))

    if input("Correct? [y/n]: ").lower() == 'y':
        c.put('ether_wake.template', '/tmp/ether_wake.template')
        c.run(f"sed -i 's|/usr/sbin/etherwake \\$mac_address|sudo /usr/sbin/etherwake -i {eth_name} \\$mac_address|' /tmp/ether_wake.template")
        c.sudo('mv /tmp/ether_wake.template /etc/maas/templates/power/')
        c.sudo('echo "maas ALL= NOPASSWD: /usr/sbin/etherwake" >> /etc/sudoers.d/99-maas-sudoers')
        print(green("Wake-on-LAN configured."))
    else:
        print(red("Warning: Wake-on-LAN not configured!"))
