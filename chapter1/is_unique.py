def is_unique(str):
    """
    >>> is_unique('cat')
    True

    >>> is_unique('tat')
    False
    """
    letters = []
    for letter in str:
        if letter in letters:
            return False
        else:
            letters.append(letter)
    return True

    # dict_str =  {}
    # for letter in str:
    #     dict_str[letter] = dict_str.get(letter, 0) + 1
    # print dict_str


    # print dict_str.values()
    # if dict_str.values() == 1:
    #     print True
    # else:
    #     print False


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print