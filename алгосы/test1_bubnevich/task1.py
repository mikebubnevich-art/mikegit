import sys

def build_matrix_with_anti_diagonal(sequence):
    n = len(sequence)
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][n - 1 - i] = sequence[i]
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{elem:4}' for elem in row))

def main():
    if len(sys.argv) < 2:
        print("Usage: python task1.py <num1> <num2> ...")
        sys.exit(1)
    
    if len(sys.argv) == 2 and ',' in sys.argv[1]:
        sequence = list(map(int, sys.argv[1].split(',')))
    else:
        sequence = list(map(int, sys.argv[1:]))
    
    if not sequence:
        print("Последовательность не должна быть пустой")
        sys.exit(1)
    
    matrix = build_matrix_with_anti_diagonal(sequence)
    
    print("Исходная последовательность:", sequence)
    print("\nПостроенная матрица (числа на побочной диагонали):")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
