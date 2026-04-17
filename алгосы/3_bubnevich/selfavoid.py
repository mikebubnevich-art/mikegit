import sys
import random
import matplotlib.pyplot as plt

def main():
   
    if len(sys.argv) != 3:
        print("invalid input")
        sys.exit(1)
    
    
    n = int(sys.argv[1])
    output_file = sys.argv[2]
    
    
    start_x = n // 2 + 1
    start_y = n // 2 + 1
    
    
    x = [start_x]
    y = [start_y]
    
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_x - 1][start_y - 1] = True  
    
    
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  
    
    
    while True:
        current_x = x[-1]
        current_y = y[-1]
        
        
        possible_dirs = []
        
        for dx, dy in directions:
            new_x = current_x + dx
            new_y = current_y + dy
            
            
            if 1 <= new_x <= n and 1 <= new_y <= n:
                
                if not visited[new_x - 1][new_y - 1]:
                    possible_dirs.append((dx, dy))
        
        
        if not possible_dirs:
            break
        
        
        dx, dy = random.choice(possible_dirs)
        
        
        new_x = current_x + dx
        new_y = current_y + dy
        x.append(new_x)
        y.append(new_y)
        visited[new_x - 1][new_y - 1] = True
    
    
    plt.figure(figsize=(8, 8))
    
    
    plt.grid(True)
    
    
    plt.plot(x, y, linewidth=3, color='black', alpha=0.7)
    
    
    plt.plot([x[0]], [y[0]], 'ro', markersize=8, )
    plt.plot([x[-1]], [y[-1]], 'bo', markersize=8, )
    
    
    plt.xlim(1, n)
    plt.ylim(1, n)
    
    
    ticks = list(range(1, n + 1))
    plt.xticks(ticks)
    plt.yticks(ticks)
    
    
    
    plt.legend()
    
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    

if __name__ == "__main__":
    main()