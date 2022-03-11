def func_counter(func):
    def wrapper(*args):
        wrapper.counter += 1
        return func(*args)

    wrapper.counter = 0
    return wrapper
