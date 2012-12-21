# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from flask import request
from flask.exceptions import JSONBadRequest

from fridge.wrappers import JSONResponse


def valid_json():
    try:
        request.json
    except JSONBadRequest:
        return JSONResponse({"message": "Badly formatted supplied Json datas"},
                            status=400)
