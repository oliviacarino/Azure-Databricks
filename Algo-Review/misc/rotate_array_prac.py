# practice for rotating an array to the right by d positions

def rotate(nums, k):
    #k = k % len(nums)
    l, r = 0, len(nums) - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

# Driver code
arr = [1, 2, 3, 4, 5] # [4, 5, 1, 2, 3]
k = 2
print(arr)
rotate(arr, k)
print(arr)
