import sys

def generate_scores():
    scores = []
    
    for sector in range(1, 21):
        scores.append(sector)
        scores.append(sector * 2)
        scores.append(sector * 3)
    
    scores.append(25)
    scores.append(50)
    
    return sorted(set(scores))

def main():
    if len(sys.argv) < 2:
        print("Usage: python task3.py <remaining_points>")
        sys.exit(1)
    
    remaining = int(sys.argv[1])
    
    if remaining < 2 or remaining > 180:
        print("Невозможно завершить за 3 броска")
        return
    
    all_scores = generate_scores()
    doubles = [sector * 2 for sector in range(1, 21)] + [50]
    
    combinations = []
    
    for first in all_scores:
        for second in all_scores:
            for third in doubles:
                if first + second + third == remaining:
                    combinations.append([first, second, third])
    
    print(combinations)

if __name__ == "__main__":
    main()
