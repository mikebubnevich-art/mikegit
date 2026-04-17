import sys
import csv
import matplotlib.pyplot as plt

def calculate_mean_std(values):
    """Вычисляет среднее и стандартное отклонение без использования numpy"""
    n = len(values)
    if n == 0:
        return 0, 0
    
    
    mean = sum(values) / n
    
    
    variance = sum((x - mean) ** 2 for x in values) / n
    std = variance ** 0.5
    
    return mean, std

def sort_countries_by_value(countries_dict, reverse=True):
    """Сортирует словарь стран по значениям без использования встроенной sorted"""
    items = list(countries_dict.items())
    
    
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if (reverse and items[j][1] < items[j + 1][1]) or \
               (not reverse and items[j][1] > items[j + 1][1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items

def main():
    
    if len(sys.argv) != 4:
        print("Использование: python worldbank.py <файл_данных> <год> <файл_для_сохранения>")
        sys.exit(1)
    
    
    data_file = sys.argv[1]
    year = sys.argv[2]
    output_file = sys.argv[3]
    
    
    countries_list = [
        "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", 
        "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", 
        "Australia", "Austria", "Azerbaijan", "Bahamas, The", "Bahrain", 
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
        "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", 
        "Brazil", "British Virgin Islands", "Brunei Darussalam", "Bulgaria", 
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", 
        "Canada", "Cayman Islands", "Central African Republic", "Chad", 
        "Chile", "China", "Colombia", "Comoros", "Congo, Dem. Rep.", 
        "Congo, Rep.", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", 
        "Curacao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", 
        "Dominican Republic", "Ecuador", "Egypt, Arab Rep.", "El Salvador", 
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", 
        "Faroe Islands", "Fiji", "Finland", "France", "French Polynesia", 
        "Gabon", "Gambia, The", "Georgia", "Germany", "Ghana", "Gibraltar", 
        "Greece", "Greenland", "Grenada", "Guam", "Guatemala", "Guinea", 
        "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
        "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Ireland", 
        "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
        "Kazakhstan", "Kenya", "Kiribati", "Korea, Dem. People's Rep.", 
        "Korea, Rep.", "Kosovo", "Kuwait", "Kyrgyz Republic", "Lao PDR", 
        "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
        "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", 
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
        "Mauritius", "Mexico", "Micronesia, Fed. Sts.", "Moldova", "Monaco", 
        "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", 
        "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", 
        "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", 
        "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", 
        "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
        "Poland", "Portugal", "Puerto Rico (US)", "Qatar", "Romania", 
        "Russian Federation", "Rwanda", "Samoa", "San Marino", 
        "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", 
        "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten (Dutch part)", 
        "Slovak Republic", "Slovenia", "Solomon Islands", "Somalia, Fed. Rep.", 
        "South Africa", "South Sudan", "Spain", "Sri Lanka", "St. Kitts and Nevis", 
        "St. Lucia", "St. Martin (French part)", "St. Vincent and the Grenadines", 
        "Sudan", "Suriname", "Sweden", "Switzerland", "Syrian Arab Republic", 
        "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
        "Trinidad and Tobago", "Tunisia", "Turkiye", "Turkmenistan", 
        "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", 
        "United Arab Emirates", "United Kingdom", "United States", "Uruguay", 
        "Uzbekistan", "Vanuatu", "Venezuela, RB", "Viet Nam", 
        "Virgin Islands (U.S.)", "Yemen, Rep.", "Zambia", "Zimbabwe"
    ]
    
    
    countries_data = {}
    indicator_name = ""
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  
            
            
            try:
                year_index = header.index(year)
            except ValueError:
                print(f"Ошибка: Год {year} не найден в файле")
                sys.exit(1)
            
            
            for row in reader:
                if len(row) < max(5, year_index + 1):
                    continue
                
                country = row[0].strip()
                if country in countries_list:
                    try:
                        
                        value = float(row[year_index]) if row[year_index] else None
                        if value is not None and not isinstance(value, str):
                            countries_data[country] = value
                    except (ValueError, IndexError):
                        continue
                
                
                if not indicator_name and len(row) > 1:
                    indicator_name = row[1].strip()
    
    except FileNotFoundError:
        print(f"Ошибка: Файл {data_file} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
    
    
    if not countries_data:
        print("Ошибка: Не найдено данных для указанного года и списка стран")
        sys.exit(1)
    
    
    values = list(countries_data.values())
    
    
    mean, std = calculate_mean_std(values)
    
    
    abnormal_countries = {}
    for country, value in countries_data.items():
        if value < mean - std or value > mean + std:
            abnormal_countries[country] = value
    
    
    sorted_abnormal = sort_countries_by_value(abnormal_countries, reverse=True)
    
    
    top_abnormal = sorted_abnormal[:10]
    
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8), 
                                    gridspec_kw={'width_ratios': [2, 1]})
    
    
    countries_names = list(countries_data.keys())
    countries_vals = list(countries_data.values())
    
    
    countries_sorted = sort_countries_by_value(countries_data, reverse=False)
    if countries_sorted:
        countries_names, countries_vals = zip(*countries_sorted)
    
    
    x_positions = range(len(countries_names))
    ax1.scatter(x_positions, countries_vals, alpha=0.6, s=30, color='blue', label='Страны')
    
    
    ax1.axhline(y=mean, color='red', linestyle='-', linewidth=2, label=f'Среднее: {mean:.2f}')
    
    
    ax1.axhline(y=mean - std, color='green', linestyle='--', linewidth=1.5, 
                label=f'mean - σ: {mean - std:.2f}')
    ax1.axhline(y=mean + std, color='green', linestyle='--', linewidth=1.5,
                label=f'mean + σ: {mean + std:.2f}')
    
    
    ax1.axhspan(mean - std, mean + std, alpha=0.2, color='green')
    
    
    ax1.set_xlabel('Страны')
    ax1.set_ylabel('Значение показателя')
    ax1.set_title(f'Значения по странам за {year} год')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    
    ax1.set_xticks([])
    
   
    ax2.axis('off')
    
    
    info_text = f"Показатель:\n{indicator_name}\n\n"
    info_text += f"Статистика за {year}:\n"
    info_text += f"Среднее (μ): {mean:.2f}\n"
    info_text += f"Ст. отклонение (σ): {std:.2f}\n"
    info_text += f"Диапазон: [{mean - std:.2f}, {mean + std:.2f}]\n\n"
    info_text += f"Всего стран: {len(countries_data)}\n"
    info_text += f"Аномальных: {len(abnormal_countries)}\n\n"
    
    info_text += "Топ-10 аномальных стран:\n"
    info_text += "=" * 30 + "\n"
    
    for i, (country, value) in enumerate(top_abnormal, 1):
        status = "выше" if value > mean + std else "ниже"
        info_text += f"{i}. {country[:20]:<20} {value:>8.2f} ({status})\n"
    
    
    ax2.text(0.05, 0.95, info_text, transform=ax2.transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    

    
    plt.tight_layout()
    
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
if __name__ == "__main__":
    main()