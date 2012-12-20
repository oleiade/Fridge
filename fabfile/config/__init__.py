# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

import s3fs
import pureftpd

from fabric.api import *


@task
def bootstrap(s3_bucket_name,
              aws_access_key,
              aws_secret_key,
              s3_endpoint="http://s3.amazonaws.com"):
    """Mounts a s3fs partition synced with provided bucket on host"""
    s3fs.credentials(aws_access_key, aws_secret_key)
    s3fs.mount(s3_bucket_name, s3_endpoint)
