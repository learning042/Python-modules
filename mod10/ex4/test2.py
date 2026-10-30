import test


def first_function():
    """This is docstring for first function"""
    print("first function")

print(first_function.__module__)
first_function = test.a_decorator(first_function)
print(first_function.__module__)
