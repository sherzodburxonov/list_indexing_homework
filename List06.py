def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    n=0
    while n<len(list1):
        if list1[n]==1:
            list1[n]="true"
        n=n+1
    return list1
print(main([1,0,0,1,0]))