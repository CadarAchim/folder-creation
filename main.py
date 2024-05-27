from pathlib import Path
import calendar

month_names = list(calendar.month_name[1:])

for i, month in enumerate(month_names):
    Path(f'2024/{i+1}.{month}').mkdir(parents=True, exist_ok=True)