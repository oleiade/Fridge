# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from __future__ import absolute_import

import json

from fabric.api import *

from .constants import PUREFTPD_CONF_DIR, PUREFTPD_OPTIONS


DEFAULT_CONFIG = {
    'ChrootEveryone': 'yes',
    'Daemonize': 'yes',
    'NoAnonymous': 'yes',
    'DisplayDotFile': 'no',
    'NoChmod': 'yes',
    'ProhibitDotFilesRead': 'yes',
}


def _is_a_camel(s):
    """Checks if a string is camelcased

    ref: http://stackoverflow.com/a/10182901/386082
    """
    return (s != s.lower() and s != s.upper())


@task
def patch(key, value):
    """Updates a single pureftpd config option

    Just supply it's camelcased key option, and
    desired value.
    """
    sudo('echo {value} > {dir}/{key}'
         .format(value, PUREFTPD_CONF_DIR, key))


@task
def put(config_file_path):
    """Updates pureftpd config according to a provided json conf file.

    File should consist in hash containing pureftp camel cased
    options as keys, and options values as values.
    """
    for key, value in json.load(config_file_path).iteritems():
        if _is_a_camel(key) and key in PUREFTPD_OPTIONS:
            path(key, value)
