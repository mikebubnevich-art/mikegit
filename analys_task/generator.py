import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Генерация данных
n_users = 1000

data = {
    'user_id': range(1, n_users + 1),
    'app_version': np.random.choice(['1.0', '1.1', '1.2', '1.3'], n_users),
    'device_type': np.random.choice(['iOS', 'Android'], n_users, p=[0.4, 0.6]),
    'session_duration_min': np.random.exponential(15, n_users).round(1),
    'screens_viewed': np.random.poisson(8, n_users),
    'time_in_app_days': np.random.exponential(30, n_users).round(0),
    'push_notifications_enabled': np.random.choice([0, 1], n_users, p=[0.3, 0.7]),
    'support_tickets': np.random.poisson(0.5, n_users),
    'converted': np.zeros(n_users, dtype=int)
}

df = pd.DataFrame(data)

# Логика конверсии с зависимостями
conversion_prob = (
    0.3 
    + (df['session_duration_min'] > 10) * 0.2
    + (df['screens_viewed'] > 5) * 0.15
    + df['push_notifications_enabled'] * 0.2
    - (df['support_tickets'] > 1) * 0.25
    - (df['app_version'] == '1.0') * 0.1
)

df['converted'] = (np.random.random(n_users) < conversion_prob).astype(int)

# Ограничиваем выбросы
df.loc[df['session_duration_min'] > 60, 'session_duration_min'] = 60
df.loc[df['screens_viewed'] > 20, 'screens_viewed'] = 20

#  СОХРАНЯЕМ CSV-ФАЙЛ
df.to_csv('user_behavior.csv', index=False, encoding='utf-8')

print(" Файл 'user_behavior.csv' успешно создан!")
print(f" Размер датасета: {df.shape[0]} строк, {df.shape[1]} столбцов")
print(f" Общая конверсия: {df['converted'].mean()*100:.1f}%")
print("\nПервые 5 строк:")
print(df.head())