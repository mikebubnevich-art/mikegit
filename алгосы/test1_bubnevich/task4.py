import sys
import random
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 3:
        print("Usage: python task4.py <word> <output_file>")
        sys.exit(1)
    
    word = sys.argv[1].upper()
    output_file = sys.argv[2]
    
    if len(word) > 25:
        print("Слово слишком длинное (максимум 25 букв)")
        sys.exit(1)
    
    max_attempts = 100
    for attempt in range(max_attempts):
        matrix = [['' for _ in range(5)] for _ in range(5)]
        positions = []
        
        start_row = random.randint(0, 4)
        start_col = random.randint(0, 4)
        matrix[start_row][start_col] = word[0]
        positions.append((start_row, start_col))
        
        success = True
        for i in range(1, len(word)):
            row, col = positions[-1]
            
            neighbors = []
            if row > 0 and matrix[row-1][col] == '':
                neighbors.append((row-1, col))
            if row < 4 and matrix[row+1][col] == '':
                neighbors.append((row+1, col))
            if col > 0 and matrix[row][col-1] == '':
                neighbors.append((row, col-1))
            if col < 4 and matrix[row][col+1] == '':
                neighbors.append((row, col+1))
            
            if not neighbors:
                success = False
                break
            
            next_row, next_col = random.choice(neighbors)
            matrix[next_row][next_col] = word[i]
            positions.append((next_row, next_col))
        
        if success:
            break
        elif attempt == max_attempts - 1:
            print("Невозможно разместить слово: тупик")
            sys.exit(1)
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == '':
                matrix[i][j] = random.choice(alphabet)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels(range(1, 6))
    ax.set_yticklabels(range(1, 6))
    ax.grid(True, linestyle='-', linewidth=1)
    
    word_positions = set(positions)
    
    for i in range(5):
        for j in range(5):
            if (i, j) in word_positions:
                ax.text(j, 4-i, matrix[i][j], fontsize=20, ha='center', va='center', color='blue', fontweight='bold')
            else:
                ax.text(j, 4-i, matrix[i][j], fontsize=20, ha='center', va='center', color='black')
    
    ax.set_title(f'Слово: {word}', fontsize=14)
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()
