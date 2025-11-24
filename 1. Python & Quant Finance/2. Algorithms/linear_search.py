def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
        


nums = [10,20,25,30,40,50]
target = 55

print(linear_search(nums,target))