def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is n copies of the front.
    """
    return str[:3] * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))