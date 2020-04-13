"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    factorial = 1
    while k > 0:
        factorial = factorial * n
        n -= 1
        k -= 1
    return factorial

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    length = len(str(n))

    prev_eight = False
    next_eight = False

    while length > 1:

        if n % 10 == 8: #first digit = 8.
            prev_eight = True
            n = n // 10
            if prev_eight and n % 10 == 8: #first digit = 8 and second digit = 8
                next_eight = True
            else: #first digit = 8 and second digit != 8
                prev_eight = False
                n = n // 10

        else: #first digit != 8.       
            n = n // 10

        length -= 1

    return next_eight



    