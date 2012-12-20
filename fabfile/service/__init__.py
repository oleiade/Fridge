# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from fabric.api import task

import pureftpd


@task
def start_all():
    """Starts all the fridge services on hosts"""
    pureftpd.start()
