import sys
def binary_search(words,prefix):
    left = 0 
    right = len(words) - 1
    first_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if words[mid].startswith(prefix):
            first_index = mid
            right = mid - 1
        elif words[mid] < prefix:
            left = mid + 1
        else:
            right = mid - 1 
    return first_index
def find_words_with_prefix(filename, prefix):
    try:
        with open (filename,  'r' , encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    if not words or not prefix:
        print("Error: The file is empty or the prefix is empty.")
        return []
    first_index = binary_search(words, prefix)
    if first_index == -1:
        return []
    result = []
    i = first_index
    while i < len(words) and words[i].startswith(prefix):
        result.append(words[i])
        i += 1
    return result
def main():
    if len(sys.argv) != 3:
        print("Usage: python findprefix.py <filename> <prefix>")
        sys.exit(1)
    filename = sys.argv[1]
    prefix = sys.argv[2]
    result = find_words_with_prefix(filename, prefix)
    if result:
            print(result)
    else:
        print([])
if __name__ == "__main__":
    main()