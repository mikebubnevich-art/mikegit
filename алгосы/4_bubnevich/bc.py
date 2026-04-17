import sys
from itertools import permutations

def get_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def generate_all_numbers(length):
    digits = '123456789'
    numbers = []
    for perm in permutations(digits, length):
        numbers.append(''.join(perm))
    return sorted(numbers)

def main():
    if len(sys.argv) != 2:
        return
    
    secret = sys.argv[1]
    
    if not secret.isdigit() or len(secret) < 2 or len(secret) > 9:
        print("Invalid input")
        return
    
    if '0' in secret:
        print("Invalid input")
        return
    
    if len(set(secret)) != len(secret):
        print("Invalid input")
        return
    
    length = len(secret)
    candidates = generate_all_numbers(length)
    attempts = []
    
    while True:
        guess = candidates[0]
        bulls, cows = get_bulls_and_cows(secret, guess)
        
        new_candidates = []
        for cand in candidates:
            b, c = get_bulls_and_cows(cand, guess)
            if b == bulls and c == cows:
                new_candidates.append(cand)
        
        attempts.append([int(guess), (bulls, cows), len(new_candidates)])
        candidates = new_candidates
        
        if len(candidates) == 1:
            break
    
    print(attempts)

if __name__ == "__main__":
    main()