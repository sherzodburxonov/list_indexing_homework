def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if list_num[0]>list_num[-1]:
        s=list_num[0]
    else:
        s=list_num[-1]
    return s
print(main([5,32,4,5,9]))