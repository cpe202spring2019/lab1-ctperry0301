
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
    if int_list == None:
        raise ValueError("")
    
    # >= high???????
    if low > high or len(int_list) == 0: # first base case
        return None
    
    #This will only work for first time, need to incorporate low and high
    mid = int_list[(low + high) // 2]
    
    if target == mid: #second base case
        #return index of the target
        return int_list[(low + high) // 2]
     
    else:
        if target > mid: #recursion 1, low should change
        #mid is the number at the position, not the index
            low = (low + high) // 2
            return bin_search(target, low + 1, high, int_list)
        elif target < mid: #recursion 2, high should change, low + 1
            high = (low + high) // 2
            return bin_search(target, low, high, int_list)
