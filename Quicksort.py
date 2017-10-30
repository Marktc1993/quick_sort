
def quick_sort(arr):
    if len(arr) <=1:
        return arr
# This is picking the middle index value.
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([1,2,3,4,5,53,2,0,2,3]))
