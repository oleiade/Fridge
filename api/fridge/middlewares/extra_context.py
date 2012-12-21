# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.


from flask import g


def get_or_create(key, value=None):
    """Retrieves or create a key/value from the request extra_context.
    If key is found, it is returned, that simple.
    If not, and a value has been passed, the key is set and returned.

    .. usage :: In most cases you'll want to pass a lambda as value,
    in order for the value to be actually generated only if it has
    to be used.
    Example:
        * get_or_create('site', Site(10)) would actually generate the Site
    instance whether you actually use it to set the value or not.
        * when get_or_create('site', lambda: Site(10)) will call the lambda
    if and only if the value has to be set. Lazyness rules.

    Parameters
    ----------
    key : string
    value : object or lambda

    Returns
    -------
    value : object
            The actual value stored at the request extra_context key.
    """
    if not hasattr(g, key):
        value = value() if callable(value) else value
        setattr(g, key, value)
    return getattr(g, key)


def get(key):
    return getattr(g, key) if hasattr(g, key) else None


def set(key, value):
    value = value() if callable(value) else value
    setattr(g, key, value)
    return getattr(g, key)


def unset(obj):
    """Unsets a/some key(s) from the extra_context

    Parameters
    ----------
    obj : String | list | tuple
          key(s) to unset from extra_context
    """
    if not isinstance(obj, (list, tuple)):
        obj = [obj]
    map(g.__delattr__, obj)