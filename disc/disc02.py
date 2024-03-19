# Q2: Make Keeper
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        i = 0
        while i < n:
            i += 1
            if cond(i):
                print(i)
        return
    return f

# Q3: Digit Finder
def find_digit(k):
    """Returns a function that returns the kth digit of x.
    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
"""
    assert k > 0
    "*** YOUR CODE HERE ***"
    return lambda x : x // 10**(k-1) % 10

# Q4: Match Maker
def match_k(k):
    """Returns a function that checks if digits k apart match.
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if find_digit(1)(x) != find_digit(1+k)(x):
                return False
            x //= 10
        return True
    return check


def print_sums(n): 
    print(n)
    def next_sum(k):
        return print_sums(n+k) 
    return next_sum


# fall2020 disc
# https://inst.eecs.berkeley.edu/~cs61a/fa20/

"""
This module provides a function print_delayed, which returns a new function that delays printing.

# doctest: +ELLIPSIS
"""
def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same behavior.
    # doctest: +ELLIPSIS
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed...>
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print



def print_n(n): 
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print> 
    """
    def inner_print(x):
        if n<=0:
            print("done")
        else: print(x)
        return print_n(n-1)
    return inner_print

