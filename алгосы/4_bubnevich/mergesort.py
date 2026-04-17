import sys

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 mergesort.py <file_path> [k]")
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
    
    sorted_numbers = mergesort(numbers)
    
    result = sorted_numbers[:k]
    print(result)

if __name__ == "__main__":
    main()