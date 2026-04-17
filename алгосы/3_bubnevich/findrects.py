import sys
def count_rectangles(filename):
    try:
        with open(filename, 'r') as f:
            matrix = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    if not matrix:
        print("Error: The file is empty.")
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range (rows):
        for j in range (cols):
            if matrix[i][j] == '1':
                if (i  == 0 or matrix[i-1][j] == '0') and (j == 0 or matrix[i][j-1] == '0'):
                    count += 1
    return count
def main():
    if len(sys.argv) != 2:
        print("Usage: python count_rectangles.py <filename>")
        return
    filename = sys.argv[1]
    result = count_rectangles(filename)
    print(result)
if __name__ == "__main__":
    main()
