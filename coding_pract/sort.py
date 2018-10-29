def sort_num(num):
    """sort
        >>> sort_num([3,6,2,5,1,4])
        [1,2,3,4,5,6]
    """
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                num[j+1],num[j] = num[j], num[j+1]
    print num
    
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
