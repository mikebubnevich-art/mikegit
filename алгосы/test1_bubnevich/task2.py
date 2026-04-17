import csv
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python task2.py <csv_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    sales_by_date = defaultdict(int)
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            date_idx = None
            amount_idx = None
            
            for i, col in enumerate(header):
                if col == 'Дата':
                    date_idx = i
                elif col == 'Сумма':
                    amount_idx = i
            
            if date_idx is None or amount_idx is None:
                print("Ошибка: в файле отсутствуют колонки 'Дата' или 'Сумма'")
                sys.exit(1)
            
            for row in reader:
                date = row[date_idx]
                amount = int(row[amount_idx])
                sales_by_date[date] += amount
        
        result = [[date, total] for date, total in sorted(sales_by_date.items())]
        print(result)
    
   
if __name__ == "__main__":
    main()
