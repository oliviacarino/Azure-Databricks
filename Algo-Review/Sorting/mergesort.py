# Merge Sort Review
# https://www.youtube.com/watch?v=cVZMah9kEjI
# Time: O(nlogn), Space: O(n)
n
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]   # aux array to store left half of arr, (0, mid point)
        right_arr = arr[len(arr)//2:]  # aux array to store right half of arr, (mid point, len(arr))

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # final merged array idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # handle left over elements in either left or right arrays
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def main():
    #arr = [3,4,1,1,20,18,17,-1,-6]
    arr = [3, 1, 2, 4]
    print(f"before sorting: {arr}")
    merge_sort(arr)
    print(f"after sorting: {arr}")

main()
