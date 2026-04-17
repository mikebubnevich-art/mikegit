import sys

def build_spiral(n):
    if n == 1:
        return [[1]]
    
    if n == 2:
        return [
            [4, 3],
            [1, 2]
        ]

    inner_matrix = build_spiral(n - 2)
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n - 2):
        for j in range(n - 2):
            matrix[i + 1][j + 1] = inner_matrix[i][j]
            
    start_val = (n - 2) ** 2 + 1
    current_val = start_val
    
    if n % 2 != 0:
        mid = n // 2
        
        for r in range(mid, -1, -1):
            matrix[r][n - 1] = current_val
            current_val += 1
            
        for c in range(n - 2, -1, -1):
            matrix[0][c] = current_val
            current_val += 1
            
        for r in range(1, n):
            matrix[r][0] = current_val
            current_val += 1
            
        for c in range(1, n):
            matrix[n - 1][c] = current_val
            current_val += 1
            
    else:
        for r in range(1, n):
            matrix[r][0] = current_val
            current_val += 1
            
        for c in range(1, n):
            matrix[n - 1][c] = current_val
            current_val += 1
            
        for r in range(n - 2, -1, -1):
            matrix[r][n - 1] = current_val
            current_val += 1
            
        for c in range(n - 2, -1, -1):
            matrix[0][c] = current_val
            current_val += 1
            
    return matrix

def main():
    if len(sys.argv) < 2:
        return
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        return

    if n <= 0:
        return

    result_matrix = build_spiral(n)
    print(result_matrix)

if __name__ == "__main__":
    main()