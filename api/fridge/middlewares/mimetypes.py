from flask import request
from flask.exceptions import JSONBadRequest

from botify.api.wrappers import JSONResponse


def valid_json():
    try:
        request.json
    except JSONBadRequest:
        return JSONResponse({"message": "Badly formatted supplied Json datas"},
                            status=400)
