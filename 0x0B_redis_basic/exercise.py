#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis data store.
It includes decorators to track performance metrics like call counts and
execution history, as well as a replay function to display logs.
"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments a counter in Redis every time the
    decorated method is called, using the method's __qualname__ as key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Increments the Redis key named after the method's qualified name
        and returns the result of the original method execution.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of inputs and outputs for a
    particular function within Redis lists.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Appends the string representation of arguments to the inputs list
        and the final return value to the outputs list in Redis.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function, showing
    the total call count along with inputs and outputs history.
    """
    local_redis = getattr(method.__self__, "_redis", None)
    if not isinstance(local_redis, redis.Redis):
        return

    qualname = method.__qualname__
    inputs_key = f"{qualname}:inputs"
    outputs_key = f"{qualname}:outputs"

    inputs = local_redis.lrange(inputs_key, 0, -1)
    outputs = local_redis.lrange(outputs_key, 0, -1)

    print(f"{qualname} was called {len(inputs)} times:")

    for inp, outp in zip(inputs, outputs):
        input_str = inp.decode("utf-8")
        output_str = outp.decode("utf-8")
        print(f"{qualname}(*{input_str}) -> {output_str}")


class Cache:
    """
    Cache class for managing data storage inside a Redis database instance.
    It handles initialization, database flushing, data persistence, and
    tracking execution counts and histories.
    """

    def __init__(self) -> None:
        """
        Initializes the Redis client instance as a private variable
        and flushes the current database to ensure a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random UUID string key, stores the provided data
        in Redis using that key, and returns the generated key string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieves data from Redis for the given key. If a callable function
        'fn' is provided, it transforms the data before returning it.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis as a string by decoding the bytes
        using UTF-8 encoding.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis and converts it to an integer.
        """
        return self.get(key, fn=int)
