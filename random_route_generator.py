import pandas as pd
from datetime import datetime, timedelta
import random


def generate_dates(start_date, end_date) -> datetime:
    days_between = (end_date - start_date).days
    random_day = random.randint(0, days_between)
    date = start_date + timedelta(days=random_day)

    while date.weekday() >= 5:
        random_day = random.randint(0, days_between)
        date = start_date + timedelta(days=random_day)

    return date.strftime("%d.%m.%Y")


def generate_times():
    start_hour = random.randint(6, 16)
    start_minute = random.randint(0, 59)
    start_time = datetime.strptime(f"{start_hour}:{start_minute}", "%H:%M")

    # Check if is rush hour
    if 7 <= start_hour <= 9 or 16 <= start_hour <= 18:
        is_rush_hour = True
        duration = random.randint(50, 120)
    else:
        is_rush_hour = False
        duration = random.randint(42, 48)

    arrived_time = start_time + timedelta(minutes=duration)
    start_at = start_time.strftime("%H:%M")
    arrived_at = arrived_time.strftime("%H:%M")

    return start_at, arrived_at, duration, is_rush_hour


csv_file_path = 'data/dataset_acme_routes.csv'
routes = pd.read_csv(csv_file_path, delimiter=";")

start_date = datetime.strptime("01.01.2022", "%d.%m.%Y")
end_date = datetime.strptime("01.05.2024", "%d.%m.%Y")

for _ in range(1000):
    day_date = generate_dates(start_date, end_date)
    start_at, arrived_at, duration, is_rush_hour = generate_times()

    weather_conditions = random.randint(1, 4)
    seasonal_happening = random.randint(0, 1)
    traffic_density = random.randint(1, 3)

    if traffic_density == 1:
        duration = duration + random.randint(30, 90)
        arrived_at = datetime.strptime(arrived_at, "%H:%M") + timedelta(minutes=duration)
        arrived_at = arrived_at.strftime("%H:%M")

    if weather_conditions <= 2:
        duration = duration + random.randint(5, 15)
        arrived_at = datetime.strptime(arrived_at, "%H:%M") + timedelta(minutes=duration)
        arrived_at = arrived_at.strftime("%H:%M")

    routes = routes._append({
        'date': day_date,
        'route_from': 'Dufourstrasse 8, CH-5000 Aarau',
        'route_to': 'Acme Clinic, Seidenhofstrasse 10, CH-6003 Luzern',
        'start_at': start_at,
        'arrived_at': arrived_at,
        'duration_in_m': duration,
        'is_rush_hour': is_rush_hour,
        'weather_conditions': weather_conditions,
        'seasonal_happening': seasonal_happening,
        'traffic_density': traffic_density
    }, ignore_index=True)

routes.to_csv(csv_file_path, index=False, sep=";")