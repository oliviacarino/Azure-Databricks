# Kadane's Algorithm
# Used for finding the max sum contiguous sub_array when negatives are present

def kadane(arr):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(arr)):
        # update the curr max sum of the sub_arr ending at index i
        max_ending_here += arr[i]

        # max sum should be more than the current element
        max_ending_here = max(max_ending_here, arr[i])

        # update the result if the current sub_arr sum is > max_so_far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

#arr = [-8, -3, -6, -2, -5, -4]
arr = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print(kadane(arr))
