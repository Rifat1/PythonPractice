def ordered_seq_search(arr,ele):
    """
    input array must be ordered
    """
    pos=0
    found=False
    stopped=False
    while pos<len(arr) and not found and not stopped:
        if arr[pos]==ele:
            found=True
        else:
            if arr[pos]>ele:
                stopped=True
            else:    
                pos+=1
    return found
arr=[1,2,3,4,5,6,7,8,9,10]
print(ordered_seq_search(arr,12 ))