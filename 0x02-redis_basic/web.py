#!/usr/bin/env python3
"""
Module web
"""
import redis
import requests
from typing import Callable


_redis = redis.Redis()


def count_access(func: Callable) -> Callable:
    """
    Counts the number of times
    a url was accessed
    """
    def wrapper(*args, **kwargs):
        """wrapper"""
        key = "count:{}".format(args[0])
        _redis.incr(key)
        return func(*args, **kwargs)
    return wrapper


def get_cache(func: Callable) -> Callable:
    """
    Counts the number of times
    a url was accessed
    """
    def wrapper(*args, **kwargs):
        """wrapper"""
        key = "result:{}".format(args[0])
        if _redis.exists(key):
            data = _redis.get(key)
            return data.decode('utf-8')
        return func(*args, **kwargs)
    return wrapper


@get_cache
@count_access
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a
    particular URL and returns it
    """
    key = "result:{}".format(url)

    response = requests.get(url)

    _redis.set(key, response.text, ex=10)

    return response.text
