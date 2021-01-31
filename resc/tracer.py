"""Build the tracefunc decorator."""

import functools


def tracefunc(func):
    """Decorates a function to show its trace."""

    @functools.wraps(func)
    def tracefunc_closure(*args, **kwargs):
        """The closure."""
        result = func(*args, **kwargs)
        print(f"{func.__name__}(args={args}, kwargs={kwargs}) => {result}")
        return result

    return tracefunc_closure


if __name__ == "__main__":

    @tracefunc
    def fibo(num):
        """Recursive Fibo."""
        return num if num <= 1 else fibo(num - 1) + fibo(num - 2)

    fibo(5)
