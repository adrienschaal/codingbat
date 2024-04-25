def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive. Unless the parameter "negative" is True, then they both must be negative. 
    """

    if negative is True and not (a < 0 and b <0):
        return False
    elif negative is True and (a < 0 and b <0):
        return True
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)
    

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))