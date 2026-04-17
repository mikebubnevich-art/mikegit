import sys

def find_sum_sequence(filename, target_sum):
    try:
        with open(filename, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except ValueError:
        print("Ошибка: файл содержит некорректные данные")
        return None
    
    if len(numbers) < 2:
        return None
    
    left = 0
    current_sum = numbers[0] + numbers[1]
    
    if current_sum == target_sum:
        return numbers[0:2]
    
    for right in range(2, len(numbers)):
        current_sum += numbers[right]
        
        while current_sum > target_sum and left < right - 1:
            current_sum -= numbers[left]
            left += 1
        
        if current_sum == target_sum and (right - left + 1) >= 2:
            return numbers[left:right + 1]
    
    while left < len(numbers) - 1:
        if current_sum == target_sum and (len(numbers) - left) >= 2:
            return numbers[left:]
        
        if left < len(numbers) - 1:
            current_sum -= numbers[left]
            left += 1
    
    return None

def main():
    if len(sys.argv) != 3:
        print("Использование: python findsum.py <файл> <сумма>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        target_sum = int(sys.argv[2])
    except ValueError:
        print("Ошибка: сумма должна быть целым числом")
        sys.exit(1)
    
    result = find_sum_sequence(filename, target_sum)
    
    if result:
        print(result)
    else:
        print("No answer")

if __name__ == "__main__":
    main()