def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        # Extend some capabilities of func
        func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__qualname__ = func.__qualname__
    wrapper.__dict__.update(func.__dict__)
    wrapper.__wrapped__ = func
    wrapper.__module__ = func.__module__
    return wrapper


@a_decorator
def second_function():
    """This is docstring for second function"""
    print("second function")
