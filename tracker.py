def func_counter(func):
    def wrapper(*args):
        wrapper.calls += 1
        return func(*args)

    wrapper.calls = 0
    return wrapper
