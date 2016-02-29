"""
Added by wendyjan on 2/8/2016.
"""


def make_fib_list(n):
    """
    This function returns the first n Fibonacci numbers.
    They begin with [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        new_i = 2
        while new_i < n:
            fib_list.append(fib_list[new_i - 1] + fib_list[new_i - 2])
            new_i += 1
    return fib_list


if __name__ == "__main__":
    print make_fib_list(1)
    print make_fib_list(5)
    print make_fib_list(10)


