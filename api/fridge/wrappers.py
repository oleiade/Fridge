# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from flask import Response
import simplejson as json


class JSONResponse(Response):
    def __init__(self, response=None, *args, **kwargs):
        response = json.dumps(response)
        headers = kwargs.pop('headers', [])
        headers.append(('Content-Type', 'application/json'))
        super(JSONResponse, self).__init__(response, headers=headers, *args, **kwargs)
