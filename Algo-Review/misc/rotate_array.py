# Rotate an array to the right by k (in place rotation)

# [1, 2, 3, 4, 5], k = 2
def rotate(nums, k):
    k = k % len(arr)
    l, r = 0, len(arr)-1

    # reverse entire array
    # [5, 4, 3, 2, 1]
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # reverse first k elements in nums
    # [4, 5, 3, 2, 1]
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # reverse last n - k elements in nums (they'll now be in correct order)
    # [4, 5, 1, 2, 3]
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

# Driver code
arr = [1, 2, 3, 4, 5] # [4, 5, 1, 2, 3]
k = 2
print(arr)
rotate(arr, k)
print(arr)
