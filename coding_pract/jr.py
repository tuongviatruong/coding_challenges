# Please answer any or all of the following questions. You can keep your answers brief - no more than 10 lines each. Use pseudocode, Python, or Java. Thanks!

# 1) Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

# 2) Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

# 3) Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def sum_for_loop(lst):
    """Compute sum of numbers in given list using for-loop
    >>> sum_for_loop([1,2,3,4])
    10
    >>> sum_for_loop([])
    0
    """
    result = 0
    for num in lst:
        result += num
    return result


def sum_while_loop(lst):
    """Compute sum of numbers in given list using while-loop
    >>> sum_while_loop([1,2,3,4])
    10
    >>> sum_while_loop([])
    0
    """
    i=0
    result=0
    while i < len(lst):
        result+=lst[i]
        i+=1
    return result


def sum_recursion(lst):
    """Compute sum of numbers in given list using recursion
    >>> sum_recursion([1,2,3,4])
    10
    >>> sum_recursion([])
    0
    """
    if not lst:
        return 0
    return lst[0]+sum_recursion(lst[1:])

def alternate(lst1, lst2):
    """Combines two lists by alternatingly taking elements
    >>> alternate(['a', 'b', 'c'],[1, 2, 3])
    ['a', 1, 'b', 2, 'c', 3]

    """
    result = []

    i=0
    while i < len(lst1):
        result.append(lst1[i])
        result.append(lst2[i])
        i+=1
    return result

def fibonacci():
    """Computes the list of the first 100 Fibonacci numbers"""
    n=100
    answer = []
    fib = [0,1]

    while len(fib) == n:
        fib.append(fib[-2]+fib[-1])

    return fib

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
