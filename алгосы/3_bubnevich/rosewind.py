import math 
import sys
import csv
import matplotlib.pyplot as plt
def wind_direction(wdir):
    if wdir is None or wdir == '':
        return  None 
    try:
        angle = float(wdir)
    except ValueError:
        return None  
    angle = angle % 360
    if (angle >= 337.5 or angle < 22.5):
        return 0
    elif angle < 67.5:
        return 1
    elif angle < 112.5:
        return 2
    elif angle < 157.5:
        return 3
    elif angle < 202.5:
        return 4
    elif angle < 247.5:
        return 5
    elif angle < 292.5:
        return 6
    elif angle < 337.5:
        return 7
    else:
        return 0
    
def read_file(filename):
    counts = [0] * 8
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            sample = f.read(1024)
            f.seek(0)
            if ';' in sample:
                delimiter = ';'
            else:
                delimiter = ','
            reader = csv.DictReader(f,delimiter=delimiter)
            if 'wdir' not in reader.fieldnames:
                print("error, no wdir")
                return None
            for row in reader:
                idx = wind_direction(row['wdir'])
                if idx is not None:
                    counts[idx] += 1
    except FileNotFoundError:
        print(f"file {filename} is not found")
        return None 
    except Exception as e:
        print(f"error, while reading file {e}")
        return None
    return counts

def plot_rose(counts,output_filename):
    directions = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
    angles_rad = [math.radians(90-i*45) for i in range(8)]
    fig, ax = plt.subplots(figsize=(10,10))
    max_count = max(counts) if max(counts) > 0 else 1
    for i, (count, angle) in enumerate(zip(counts, angles_rad)):
        length = count / max_count * 100 
        if count > 0:
            x = [0, length * math.cos(angle)]
            y = [0, length * math.sin(angle)]
            ax.plot(x, y, 'b-', linewidth=2, alpha=0.7)
            ax.arrow(x[0], y[0], x[1]-x[0], y[1]-y[0], 
                head_width=3, head_length=3, fc='blue', ec='blue', alpha=0.7)
            text_x = length * math.cos(angle) * 1.1
            text_y = length * math.sin(angle) * 1.1
            ax.text(text_x, text_y, str(count), 
                fontsize=9, ha='center', va='center')
        label_radius = max_count / max_count * 110
        label_x = label_radius * math.cos(angle)
        label_y = label_radius * math.sin(angle)
        ax.text(label_x, label_y, directions[i], 
            fontsize=12, fontweight='bold', ha='center', va='center')
    for r in range(25, 101, 25):
        circle = plt.Circle((0, 0), r, fill=False, linestyle='--', alpha=0.3, color='gray')
        ax.add_artist(circle)
        ax.text(r, 0, f'{int(r * max_count / 100)}', 
            fontsize=8, ha='left', va='center', alpha=0.5)

    
    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    ax.set_aspect('equal')
    
    
    ax.grid(True, linestyle=':', alpha=0.3)
    
    
    ax.set_xticks([])
    ax.set_yticks([])
    
   
    plt.title('Роза ветров для Минска (2025 год)', fontsize=16, fontweight='bold')
    
   
    ax.text(95, -110, f'Всего записей: {sum(counts)}', 
           fontsize=10, ha='right', va='bottom')
    
    
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    

def main():
    if len(sys.argv) != 3:
        print("Использование: python rosewind.py <входной_csv_файл> <выходной_файл_графика>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    
    counts = read_file(input_file)
    
    if counts is None:
        sys.exit(1)
    
    
    
    
    
    plot_rose(counts, output_file)

if __name__ == "__main__":
    main()
            
            
                       