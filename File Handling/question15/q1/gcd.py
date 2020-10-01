def find_the_hcf_using_recursion(first, second):
    if first == second:
        return first
    if first == 0 or second == 0:
        return 0

    if first > second:
        return find_the_hcf_using_recursion(first-second,second)
    return find_the_hcf_using_recursion(first, second-first)

def find_the_hcf(first, second):
    if first < 0:
        first = -first
    if second<0:
        second = -second
    while(first!=second):
        if first>second:
            first-=second
        else:
            second-=first
    return first



print(find_the_hcf_using_recursion(81,153))