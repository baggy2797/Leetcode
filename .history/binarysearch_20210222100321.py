def BinarySearch(arr,high,low,key):
    if high < low:
        return -1
    
    mid = (high+low)/2
    
    if key == arr[int(mid)]:
        return mid

    if key > arr[int(mid)]:
        return BinarySearch(arr,mid+1,low,key)

    return BinarySearch(arr,high,mid-1,key)

arr = [5,6,7,8,9,10]
n =len(arr)
key = 10

print("Index:", int(BinarySearch(arr, 0, n-1, key) )) 