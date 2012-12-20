# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from __future__ import absolute_import

from fabric.api import *
from fabtools.service import *

from ..config.constants import PUREFTPD_SERVICE_NAME


@task
def start(service_name=PUREFTPD_SERVICE_NAME):
    if not service.is_running(service_name):
        service.start(service_name)


@task
def stop(service_name=PUREFTPD_SERVICE_NAME):
    if service.is_running(service_name):
        service.stop(service_name)


@task
def restart(service_name=PUREFTPD_SERVICE_NAME):
    service.restart(service_name)
