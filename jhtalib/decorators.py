# Import Built-Ins:
import functools
import time

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Finished {!r} in {:.8f} secs.'.format(func.__name__, run_time))
        return value

    return wrapper_timer

