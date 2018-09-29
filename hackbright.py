def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?
    These are fine::

       >>> has_balanced_brackets("<ok>")
       True

       >>> has_balanced_brackets("<{ok}>")
       True

       >>> has_balanced_brackets("<[{(yay)}]>")
       True

    These are invalid, since they have too many open brackets::

       >>> has_balanced_brackets("(Oops!){")
       False

       >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
       False

    These are invalid, as they close brackets that weren't open::

       >>> has_balanced_brackets(">")
       False

       >>> has_balanced_brackets("(This has {too many} ) closers. )")
       False

    Here's a case where the number of brackets opened matches
    the number closed, but in the wrong order::

        >>> has_balanced_brackets("<{Not Ok>}")
        False

    If you receive a string with no brackets, consider it balanced::

       >>> has_balanced_brackets("No brackets here!")
       True


    """
    # stack = []

    # for k in phrase:
    #     if k == "(":
    #         stack.append(k)
    #     elif k == ")":
    #         stack.pop()
    # if stack == []:
    #     return True
    # return False

    paren = 0

    for j in phrase:
        if j == "(":
            paren += 1
        elif j == ")":
            paren -= 1
            if paren < 0:
                return False
    if paren == 0:
        return True
    return False

def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.



       >>> has_balanced_brackets("<ok>")
       True

       >>> has_balanced_brackets("<{ok}>")
       True

       >>> has_balanced_brackets("<[{(yay)}]>")
       True

    These are invalid, since they have too many open brackets:

       >>> has_balanced_brackets("(Oops!){")
       False

       >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
       False

    These are invalid, as they close brackets that weren't open::

       >>> has_balanced_brackets(">")
       False

       >>> has_balanced_brackets("(This has {too many} ) closers. )")
       False

    Here's a case where the number of brackets opened matches
    the number closed, but in the wrong order::

        >>> has_balanced_brackets("<{Not Ok>}")
        False

    If you receive a string with no brackets, consider it balanced::

       >>> has_balanced_brackets("No brackets here!")
       True

    """
    brackets = {')':'(','}':'{',']':'[','>':'<'}
    brackets_set = set(brackets.values())

    stack = []
    for l in phrase:
        if l in brackets_set:
            stack.append(l)
        elif l in brackets:
            if stack == [] or brackets[l] != stack.pop():
                return False
    return stack == []

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.
    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

    >>> add_to_zero([0, 1, 2])
    True

    """
    for i in nums:
        for j in nums:
            if i + j == 0:
                return True
    return False





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
