# Quicksort Practice
def quick_sort(arr, start, end):
    if start <= end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    e = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < e:
            i += 1
            swap(arr, i, j)
    i += 1
    swap(arr, i, end)
    return i

def main():
    arr = [3,4,1,1,20,18,17,-1,-6]
    print(f"before sorting: {arr}")
    quick_sort(arr, 0, len(arr)-1)
    print(f"after sorting: {arr}")

main()
