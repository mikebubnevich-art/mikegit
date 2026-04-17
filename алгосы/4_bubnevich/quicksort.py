import sys
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quicksort.py <file_path> [k]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        k = int(sys.argv[2])
    else:
        k = 20
    
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            if not content:
                numbers = []
            else:
                numbers = list(map(int, content.split()))
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        sys.exit(1)
    except ValueError:
        print("File contains non-integer values")
        sys.exit(1)
    
    sorted_numbers = quicksort(numbers)
    
    result = sorted_numbers[:k]
    print(result)

if __name__ == "__main__":
    main()