# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from fabric.api import *
from fabtools import require


@task
def bootstrap():
    """Bootstraps the hosts with needed packages and softs"""
    versioning()
    s3fs()
    pureftpd()


@task
def s3fs():
    """Installs s3fs file-sytem over host.

    Noticable dependencies : fuse and sshfs.
    Relies on versioning task, in order to
    be able to pull the s3fs repo.
    """
    # Install system packages for s3fs
    require.deb.packages([
        "build-essential",
        "libcurl4-openssl-dev",
        "libxml2-dev",
        "libfuse-dev",
        "comerr-dev",
        "libfuse2",
        "libidn11-dev",
        "libkrb5-dev",
        "libldap2-dev",
        "libselinux1-dev",
        "libsepol1-dev",
        "pkg-config",
        "fuse-utils",
        "sshfs",
    ])

    with cd('/tmp'):
        run('svn checkout http://s3fs.googlecode.com/svn/trunk/ s3fs-read-only')

        with cd('s3fs-read-only'):
            run('./autogen.sh')
            run('./configure')
            run('make')
            sudo('make install')


@task
def pureftpd():
    """Installs pureftpd on host"""
    # Install pureftpd packages
    require.deb.packages([
        'pure-ftpd',
        'pure-ftpd-common',
    ])


@task
def versioning():
    """Install common versioning tools on host"""
    require.deb.packages([
        'git-core',
        'mercurial',
        'subversion',
    ])
