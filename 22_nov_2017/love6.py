
# The number 6 is a truly great number. Given two int values, a and b, 
# return True if either one is 6. Or if their sum or difference is 6. 
# Note: the function abs(num) computes the absolute value of a number.


# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True
# love6(7,1) 


def love6(a, b):
    if 6 in (a, b):
        return True
    return a+b == 6 or abs(a-b) - 6 == 0 or abs(b-a) - 6 == 0


assert love6(6, 4)
assert love6(4, 6)
assert love6(4, 5) is False
assert love6(1, 5)
assert love6(-1, 7)
assert love6(1, 7)
assert love6(-3, -3) is False
assert love6(3, -3)
assert love6(-3, 3)
assert love6(0, 0) is False
assert love6(0, -6)
assert love6(-6, 0)