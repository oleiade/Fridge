# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from fabric.api import *
from fabric.contrib.files import exists


@task
def mount(bucket_name, s3_endpoint="http://s3.amazonaws.com"):
    s3fs_exec = '/usr/local/bin/s3fs'

    if not exists('/mnt/s3'):
        sudo('mkdir /mnt/s3')

    # Create mountpoint for s3fs
    sudo('{s3fs} {bucket} /mnt/s3 -o url={endpoint} -o use_cache=/tmp -o allow_other'
         .format(s3fs=s3fs_exec, bucket=bucket_name, endpoint=s3_endpoint))


@task
def umount(mountpoint='/mnt/s3'):
    if exists(mountpoint):
        sudo('umount %s' % mountpoint)


@task
def credentials(aws_access_key, aws_secret_key):
    # Generate s3fs passwd file with credentials
    sudo('echo "{accesskey}:{secretkey}" > /etc/passwd-s3fs'
         .format(accesskey=aws_access_key, secretkey=aws_secret_key))
    sudo('chmod 640 /etc/passwd-s3fs')
