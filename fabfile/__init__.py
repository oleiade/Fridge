# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

import install
import config
import service

from fabric.api import env

env.hosts = ['localhost']