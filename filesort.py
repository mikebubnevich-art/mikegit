import sys
import os
import time
import tracemalloc

def merge_sort_words_arr(arr):
    """Сортирует список слов методом слияния."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_words_arr(arr[:mid])
    right = merge_sort_words_arr(arr[mid:])
    
    return merge_words(left, right)

def merge_words(left, right):
    """Сливает два отсортированных списка слов."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def process_line(line):
    """Обрабатывает одну строку: сортирует слова внутри нее."""
    # Удаляем завершающий newline, если есть, чтобы не мешал сортировке слов, 
    # но сохраняем структуру. Слова разделены пробелами.
    stripped = line.strip()
    if not stripped:
        return ""
    words = stripped.split()
    if not words:
        return ""
    sorted_words = merge_sort_words_arr(words)
    return " ".join(sorted_words)

def merge_sort_lines_arr(lines):
    """Сортирует список строк методом слияния."""
    if len(lines) <= 1:
        return lines
    
    mid = len(lines) // 2
    left = merge_sort_lines_arr(lines[:mid])
    right = merge_sort_lines_arr(lines[mid:])
    
    return merge_lines(left, right)

def merge_lines(left, right):
    """Сливает два отсортированных списка строк."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_two_files_sorted(path1, path2, path_out):
    """
    Сливает два отсортированных файла в один отсортированный.
    Читает по одной строке из каждого, сравнивает, записывает меньшую.
    """
    with open(path1, 'r', encoding='utf-8') as f1, \
         open(path2, 'r', encoding='utf-8') as f2, \
         open(path_out, 'w', encoding='utf-8') as fout:
        
        line1 = f1.readline()
        line2 = f2.readline()
        
        while line1 and line2:
            # Сравнение строк
            if line1 <= line2:
                fout.write(line1)
                line1 = f1.readline()
            else:
                fout.write(line2)
                line2 = f2.readline()
        
        # Дописываем остаток
        while line1:
            fout.write(line1)
            line1 = f1.readline()
            
        while line2:
            fout.write(line2)
            line2 = f2.readline()

def main():
    if len(sys.argv) < 2:
        print("Usage: python filesort.py <filename>")
        return

    input_filename = sys.argv[1]
    
    if not os.path.exists(input_filename):
        print(f"File {input_filename} not found.")
        return

    # Формируем имя выходного файла
    base, ext = os.path.splitext(input_filename)
    output_filename = f"{base}_out{ext}"
    
    # Временная директория для чанков
    temp_dir = "temp_chunks"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Очистка старых временных файлов, если есть
    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))

    # 1. Чтение, обработка строк и создание начальных отсортированных чанков
    chunk_size = 1000 # Количество строк в чанке. Можно регулировать.
                      # При среднем размере строки 50 байт, 1000 строк ~ 50КБ, что очень мало.
                      # Можно увеличить до 10000 или больше для эффективности.
                      # Главное, чтобы список строк в памяти не превышал лимит.
    
    temp_files = []
    current_chunk_lines = []
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Обрабатываем строку: сортируем слова
                processed_line = process_line(line)
                # Добавляем newline обратно для корректной записи и сравнения в файлах
                if processed_line:
                    current_chunk_lines.append(processed_line + "\n")
                else:
                    current_chunk_lines.append("\n") # Пустая строка
                
                if len(current_chunk_lines) >= chunk_size:
                    # Сортируем чанк строк merge sort'ом
                    sorted_chunk = merge_sort_lines_arr(current_chunk_lines)
                    
                    # Записываем во временный файл
                    temp_filename = os.path.join(temp_dir, f"chunk_{len(temp_files)}.txt")
                    with open(temp_filename, 'w', encoding='utf-8') as tf:
                        tf.writelines(sorted_chunk)
                    
                    temp_files.append(temp_filename)
                    current_chunk_lines = []
            
            # Обработка последнего неполного чанка
            if current_chunk_lines:
                sorted_chunk = merge_sort_lines_arr(current_chunk_lines)
                temp_filename = os.path.join(temp_dir, f"chunk_{len(temp_files)}.txt")
                with open(temp_filename, 'w', encoding='utf-8') as tf:
                    tf.writelines(sorted_chunk)
                temp_files.append(temp_filename)
                
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 2. Многоэтапное слияние временных файлов (Pairwise Merge)
    # Пока файлов больше 1, сливаем их попарно
    
    while len(temp_files) > 1:
        next_level_files = []
        i = 0
        while i < len(temp_files):
            if i + 1 < len(temp_files):
                # Сливаем два файла
                f1 = temp_files[i]
                f2 = temp_files[i+1]
                merged_filename = os.path.join(temp_dir, f"merged_{len(next_level_files)}.txt")
                
                merge_two_files_sorted(f1, f2, merged_filename)
                
                next_level_files.append(merged_filename)
                
                # Удаляем старые файлы, чтобы экономить место на диске (опционально)
                try:
                    os.remove(f1)
                    os.remove(f2)
                except:
                    pass
                i += 2
            else:
                # Нечетный файл, просто переходит на следующий уровень
                next_level_files.append(temp_files[i])
                i += 1
        
        temp_files = next_level_files

    # 3. Переименование финального файла в результат
    if temp_files:
        final_temp_file = temp_files[0]
        # Копируем или переименовываем
        try:
            os.rename(final_temp_file, output_filename)
        except OSError:
            # Если переименование между разными ФС или занято, копируем
            import shutil
            shutil.copy2(final_temp_file, output_filename)
            os.remove(final_temp_file)
            
    # Очистка директории
    try:
        if os.path.exists(temp_dir):
            for f in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, f))
            os.rmdir(temp_dir)
    except:
        pass

if __name__ == "__main__":
    # Для тестирования производительности и памяти, как просили в задании:
    tracemalloc.start()
    t0 = time.time()
    
    main()
    
    elapsed_time = time.time() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Вывод статистики в stderr, чтобы не засорять stdout, если он перенаправлен
    print(f"Time: {elapsed_time:.4f}s", file=sys.stderr)
    print(f"Current memory usage: {current / 10**6:.2f}MB", file=sys.stderr)
    print(f"Peak memory usage: {peak / 10**6:.2f}MB", file=sys.stderr)