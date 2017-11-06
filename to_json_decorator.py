import functools
import json


def to_json(wrapped):
    @functools.wraps(wrapped)
    def inner(*args, **kwargs):
        result = wrapped(*args, **kwargs)
        return json.dumps(result)
    return inner
