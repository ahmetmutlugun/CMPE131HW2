import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        print(f"Total time {time.time() - start}")

    return wrapper
