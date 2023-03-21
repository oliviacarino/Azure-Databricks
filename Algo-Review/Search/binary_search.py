# Iterative and recursive implementations of Binary Search
# Time: O(logn)

# iterative imp --- Space: O(1)
def binary_search_it(lst, target):
    if len(lst) < 1:
        return -1
    low, high = 0, len(lst)
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# recursive imp --- Space: O(logn) because we use the Call Stack
def binary_search_rec(lst, low, high, target):
    # base case 1 -- search space is exhausted, target not found within lst
    if low > high:
        return -1
    mid = low + (high - low) // 2

    # base case 2 -- target is found
    if lst[mid] == target:
        return mid

    # recursive cases, discard elements to search in the LEFT half of lst
    # OR discard elements to search in the RIGHT half of lst
    elif target < lst[mid]:
        return binary_search_rec(lst, low, mid-1, target)
    else:
        return binary_search_rec(lst, mid+1, high, target)

def main():
    lst = [2,5,23,44,89,1001,1500,4000]
    print(lst)
    target = 1500
    #res = binary_search_it(lst,target)
    #print(f"index of {target} is {res}")
    res = binary_search_rec(lst,0,len(lst)-1,target)
    print(f"index of {target} is {res}")
main()
