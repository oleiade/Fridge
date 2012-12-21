# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

from functools import wraps

from flask import Response, request

from fridge.wrappers import JSONResponse
from fridge.middlewares import extra_context
from fridge.middlewares.mimetypes import valid_json

MIMETYPES_VALIDATORS = {
    'application/json': [
        valid_json,
    ]
}


def accepts(mimetypes):
    """Validates content types the resource accepts as input

    .. Usage :: in order not to interfer with the flask routing
    process, accepts validator has to be used after the app.route
    flask function decorator.

    Parameters
    ----------
    mimetype : list | tuple

    Raises
    ------
    TypeError
        Input mimetypes is neither a list or tuple

    Returns
    -------
    415 : Unsupported media type
          If received request Content-Type does not
          match with any provided mimetypes.

    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not isinstance(mimetypes, (list, tuple)):
                raise TypeError("Accepts takes a sequence as argument, %s given" % type(mimetypes))

            if not any(t == request.headers['Content-Type'] for t in mimetypes):
                return Response(status=415)

            if request.headers['Content-Type'] in MIMETYPES_VALIDATORS:
                for validator in MIMETYPES_VALIDATORS[request.headers['Content-Type']]:
                    err = validator()
                    if err:
                        return err

            return f(*args, **kwargs)

        return decorated_function
    return decorator


def validators(vs, extra_context=None):
    """Applies a sequence of validation function to a request datas
    Validation functions should take a Flask request object as input,
    and raise and error in case request is invalid. When any of the
    provided validation function raises an error, validators returns
    a JSONResponse object using the error Exception `message` and `status`.

    Validation functions should always prototype like this:
    def func(request, *args, **kwargs)

    Errors should be raised using Exception(args), and are composed
    of the `message` and `status` code to build the error Response with.

    If an error has to be raised without being catched and responded,
    you'll have to raise a specific exception, defined in api.exceptions module.

    Examples:
        def is_valid_json(request):
            if not json in request or not request.json:
                raise MyError("my error message", 400)

        @validators([is_valid_json])
        def my_view():
            ...

        will return : JSONResponse({'message': 'my error message'}, status=400)
        in case there was no valid json to use in the request.

    Parameters
    ----------
    vs : list(functions)
         Validation functions
    """
    validators = vs if isinstance(vs, (list, tuple)) else [vs]
    extra_context = {} if extra_context is None else extra_context

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                map(lambda f: f(request, **extra_context), validators)
            except Exception as err:
                if type(err) != ValidationException:
                    msg, status = err.args
                    return JSONResponse(dict(message=msg), status=status)
                else:
                    raise err
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def paginate(f):
    """Updates the extra_context with `page` and `per_page`
    in order to paginate the response. Extra_context has to be present.

    .. Nota :: Unsets `page` and `per_page` from the extra_context
    once the function has been executed.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        def resource_link(url, page, per_page, rel):
            return '<%s?page=%d&per_page=%d>; rel="%s"' % (url, page, per_page, rel)

        # Default pagination values
        page = 1
        per_page = 30

        if 'page' in request.args:
            page = int(request.args['page'])

        if 'per_page' in request.args:
            per_page = int(request.args['per_page'])

        extra_context.set('page', page)
        extra_context.set('per_page', per_page)
        extra_context.set('objects_count', 0)

        # Execute the view, and get the Response
        response = f(*args, **kwargs)

        # In order to paginate a response, objects_count has to be
        # in the extra_context. It should represent the existing resources
        # count you're trying to list.
        pages_count = extra_context.get('objects_count') / per_page

        next_page = page + 1 if (page + 1) <= pages_count else None
        prev_page = page - 1 if (page - 1) > 0 else None
        last_page = pages_count if pages_count > 0 else 1

        next_link = resource_link(request.url, next_page, per_page, "next") if next_page else ''
        prev_link = resource_link(request.url, prev_page, per_page, "prev") if prev_page else ''
        last_link = resource_link(request.url, last_page, per_page, "last")
        links = [link for link in [next_link, prev_link, last_link] if link]

        response.headers.add_header('Link', ', '.join(links))

        # Unset extra context page and per_page elems
        extra_context.unset(['page', 'per_page', 'objects_count'])

        return response

    return decorated_function
