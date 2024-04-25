def close_far(a, b, c):
    '''
    Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
    '''
    if abs(a-b) <= 1:
        if abs(a-c) >= 2 and abs(b-c) >= 2:
            return True
  
    if abs(a-c) <= 1:
        if abs(a-b) >= 2 and abs(b-c) >= 2:
            return True
    
    return False

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))