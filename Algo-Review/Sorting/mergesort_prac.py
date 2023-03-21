# Merge Sort practice

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        i = 0 # left arr ptr
        j = 0 # right arr ptr
        k = 0

        merge_sort(left_arr)
        merge_sort(right_arr)

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def main():
    arr = [3,4,1,1,20,18,17,-1,-6]
    print(f"before sorting: {arr}")
    merge_sort(arr)
    print(f"after sorting: {arr}")

main()
