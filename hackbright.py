def has_balanced_parens(phrase):
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