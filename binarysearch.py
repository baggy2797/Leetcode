def binarySearch(arr, low, high, key): 
    print("INside")
    if (high < low): 
        return -1
    # low + (high - low)/2 
    mid = (low + high)/2
    
    if (key == arr[int(mid)]): 
        return mid 

    if (key > arr[int(mid)]): 
        return binarySearch(arr, (mid + 1), high, key) 
    return (binarySearch(arr, low,(mid -1), key)) 

# Driver program to check above functions  
# Let us search 3 in below array 
arr = [-1,0,3,5,9,12]

n = len(arr) 
key = 9
print("Index:", int(binarySearch(arr, 0, n, key) )) 