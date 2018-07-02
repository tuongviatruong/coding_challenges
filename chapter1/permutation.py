def check_permutation(str1,str2):
    """Given two strings, decide if one is a permutation of the other

    >>> check_permutation("bat","tab")
    True

    >>> check_permutation("cat","bat")
    False
    """

    str1=sorted(str1)
    str2=sorted(str2)

    if str1 == str2:
        return True
    else:
        return False


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print