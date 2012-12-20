# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from functools import wraps


def with_headers(headers):
    """Middleware updating response header with provided datas.

    Parameters
    ----------
    list(tuples) : headers
                   A list of key/value headers wrapped in tuples.
                   Example :
                        [('Allow', 'GET, POST'),
                         ('Content-Type', 'application/json') ...]

    Returns
    -------
    Response : response
               Original functional call returned response, updated
               with the provided headers.

    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            response = f(*args, **kwargs)

            for header in headers:
                if not header[0] in response.headers:
                    response.headers.add(header[0], header[1])
                else:
                    response.headers.set(header[0], header[1])

            return response

        return decorated_function
    return decorator
