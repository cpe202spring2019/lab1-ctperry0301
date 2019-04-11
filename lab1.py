
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    elif int_list == None:
        raise ValueError("")
    else:
        maximum = int_list[0] #sets max as first value
        for i in int_list:
            if i > maximum: #sets max to i's value if it is greater than current max
                maximum = i
        return maximum
       

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    reversed_list = []
    if int_list == None:
        raise ValueError("")
    elif len(int_list) <= 1: #no need to reverse if there is 0 or 1 element
        return int_list
    else:
        #takes first value and appends it to list starting at 2nd value
        return reverse_rec(int_list[1:]) + [int_list[0]]
            

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = (low + high) // 2
    if int_list == None:
        raise ValueError("")
    else:
        if (low > high) or len(int_list) == 0 or low < 0 or high > len(int_list) - 1: # first base case
            return None
        elif target == int_list[mid]: #second base case
            return mid
        elif target > int_list[mid]: #recursion 1, low should change
            return bin_search(target, mid + 1, high, int_list)
        elif target < int_list[mid]: #recursion 2, high should change, low + 1
            return bin_search(target, low, mid, int_list)
