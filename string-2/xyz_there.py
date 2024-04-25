def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    '''
    return str.count('xyz') - str.count('.xyz') > 0

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))