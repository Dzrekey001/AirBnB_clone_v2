#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive from the
    contents of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    dir_name = "versions"
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p {}".format(dir_name))
        local("tar -cvzf {}/{} /web_static".format(dir_name, timestamp))

        return "{}/web_static_{}.tgz".format(dir_name, timestamp)
    except Exception as e:
        return None
