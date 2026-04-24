import sys
import random
import matplotlib.pyplot as plt

def read_ifs_file(filename):
    """
    Читает файл с коэффициентами IFS в формате:
    - Первая строка: вероятности и название
    - Затем блоки по 4 строки для x-коэффициентов и 4 строки для y-коэффициентов
    """
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # Первая строка содержит вероятности и название
    first_line = lines[0].split()
    probabilities = []
    for item in first_line:
        try:
            probabilities.append(float(item))
        except ValueError:
            continue  # Пропускаем название
    
    # Нормализуем вероятности
    prob_sum = sum(probabilities)
    if abs(prob_sum - 1.0) > 0.0001:
        probabilities = [p / prob_sum for p in probabilities]
    
    # Определяем количество преобразований
    num_transforms = len(probabilities)
    
    # Дальше идут коэффициенты: сначала все x-коэффициенты (по 3 числа), потом все y-коэффициенты (по 3 числа)
    # Обычно это 4 строки для x и 4 строки для y
    all_numbers = []
    for line in lines[1:]:
        all_numbers.extend([float(x) for x in line.split()])
    
    # Проверяем, что чисел достаточно
    expected_numbers = num_transforms * 6
    if len(all_numbers) < expected_numbers:
        raise ValueError(f"Ожидалось {expected_numbers} коэффициентов, получено {len(all_numbers)}")
    
    # Разделяем на x и y коэффициенты
    half = num_transforms * 3
    x_coeffs = all_numbers[:half]
    y_coeffs = all_numbers[half:half*2]
    
    # Формируем преобразования
    transforms = []
    for i in range(num_transforms):
        a, b, e = x_coeffs[i*3:(i+1)*3]
        c, d, f = y_coeffs[i*3:(i+1)*3]
        transforms.append([a, b, c, d, e, f])
    
    return probabilities, transforms

def apply_transform(x, y, transform):
    """Применяет аффинное преобразование"""
    a, b, c, d, e, f = transform
    new_x = a * x + b * y + e
    new_y = c * x + d * y + f
    return new_x, new_y

def main():
    if len(sys.argv) != 3:
        print("Использование: python ifs.py <файл_коэффициентов> <файл_сохранения>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Читаем коэффициенты
    try:
        probabilities, transforms = read_ifs_file(input_file)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    
    print(f"Загружено {len(transforms)} преобразований")
    print(f"Вероятности: {[f'{p:.3f}' for p in probabilities]}")
    
    # Генерация точек
    num_points = 100000
    x, y = 0.0, 0.0
    points_x = []
    points_y = []
    
    for i in range(num_points):
        # Выбираем преобразование
        r = random.random()
        cum_prob = 0
        idx = 0
        for j, p in enumerate(probabilities):
            cum_prob += p
            if r < cum_prob:
                idx = j
                break
        
        # Применяем преобразование
        x, y = apply_transform(x, y, transforms[idx])
        
        # Сохраняем после прогрева
        if i >= 100:
            points_x.append(x)
            points_y.append(y)
    
    # Определяем название фрактала по имени файла
    filename_lower = input_file.lower()
    if 'carpet' in filename_lower:
        color = 'purple'
        title = 'Ковер Серпинского'
    elif 'fern' in filename_lower:
        color = 'green'
        title = 'Папоротник'
    elif 'maple' in filename_lower:
        color = 'orange'
        title = 'Кленовый лист'
    elif 'sierpinski' in filename_lower:
        color = 'blue'
        title = 'Треугольник Серпинского'
    else:
        color = 'black'
        title = 'IFS Фрактал'
    
    # Строим график
    plt.figure(figsize=(10, 10))
    plt.scatter(points_x, points_y, s=0.1, c=color, alpha=0.7, marker='.')
    plt.axis('equal')
    plt.axis('off')
    plt.title(title, fontsize=16)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Фрактал сохранен в {output_file}")

if __name__ == "__main__":
    main()