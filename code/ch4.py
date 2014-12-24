#!/usr/bin/env python
# encoding: utf-8

import doctest

# e4.1-5
def get_max_subarray(l):
    """
    >>> get_max_subarray([10, 11, 7, 10, 6])
    3
    >>> get_max_subarray([100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, \
        106, 101, 79, 94, 90, 97])
    43
    """
    if len(l) <= 1:
        return 0
    v = [l[i] - l[i-1] for i in range(1, len(l))]
    sum = m = 0
    for i in v:
        sum = sum + i if sum + i > 0 else 0
        m = max(m, sum)
    return m

if __name__ == '__main__':
    doctest.testmod()
