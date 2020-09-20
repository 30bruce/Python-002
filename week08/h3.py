import time
import functools

def timer(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'function {func.__name__}\'s exec time: {time.time() - start}')
        return res
    
    return decorator

if __name__ == '__main__':
    @timer
    def foo(a, b):
        time.sleep(1)
    
    foo(1, 2)