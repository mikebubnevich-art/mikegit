import sys 
def buble_sort(lst):
    comparisons = 0
    swaps = 0
    arr = lst.copy()
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, comparisons, swaps
def selections_sort(lst):
    comparisons = 0
    swaps = 0
    arr = lst.copy()
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, comparisons, swaps
def insertion_sort(lst):
    comparisons = 0
    swaps = 0
    arr = lst.copy()
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
            else:
                break
        arr[j+1] = key
        if j+1 != i:
            swaps += 1    

    return arr, comparisons, swaps
if len(sys.argv) < 2:
    print("invalid input")
    sys.exit(1)
filename = sys.argv[1]
method = sys.argv[2].lower() if len(sys.argv) >= 3 else "buble"
k = int(sys.argv[3]) if len(sys.argv) >= 4 else 20
try:
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(2)
if method == "buble":
    sorted_list,comparisons, swaps = buble_sort(numbers)
elif method == "selection":
    sorted_list, comparisons, swaps = selections_sort(numbers)
elif method == "insertion":
    sorted_list, comparisons, swaps = insertion_sort(numbers)
else:
    print("Invalid sorting method. Use 'buble', 'selection', or 'insertion'.")
    sys.exit(3)
k_first = sorted_list[:k] if k < len(sorted_list) else sorted_list


print(f" ({comparisons}, {swaps}, {k_first})")    
