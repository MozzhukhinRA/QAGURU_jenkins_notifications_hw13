import random
from dataclasses import dataclass


@dataclass
class User:
    first_name = random.choice(["Max", "Pavel", "Alex", "Skot"])
    last_name = random.choice(["Kuznetsov", "Alekin", "Stepanov", "Pierro"])
    mail = f'{first_name.lower()}.{last_name.lower()}@gmail.com'
    day = random.choice(['10','11', '19', '28'])
    moth = random.choice(["April", "February", "May", "September"])
    year = random.randint(1950, 2025)
    gender = random.choice(["Male", "Female", "Other"])
    phone = f'9{random.randint(000000000, 999999999)}'
    sub = random.choice(["English", "Physics"])
    hobbies = random.choice(["Sports", "Music"])
    picture = 'photo.jpeg'
    address = random.choice(["Piter", "Ryazan"])
    region = 'Uttar Pradesh Merrut'
    full_name = f'{first_name} {last_name}'
    birth_day = f'{day} {moth},{year}'
