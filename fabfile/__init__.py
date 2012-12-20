# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

import install
import config
import service

from fabric.api import env, task


env.hosts = ['localhost']


@task
def bootstrap():
    """Deploy, configure, and start Fridge on hosts"""
    install.bootstrap()
    config.bootstrap()
    service.start_all()
