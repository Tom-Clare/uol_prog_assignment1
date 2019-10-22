def no_three_sum(a: int, b: int, c: int) -> int:

    # validate arguments
    a = fix_three(a)
    b = fix_three(b)
    c = fix_three(c)

    return a + b + c  # return sum of all three


def fix_three(n: int) -> int:
    # apply rules to any int provided

    # initialise important variables
    lower_limit = 20
    upper_limit = 29
    multiple = 3

    if n % multiple == 0 and not lower_limit < n < upper_limit:  # multiple of three and not in our range
        return 0

    return n  # passed all checks
