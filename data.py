import os
import random
import json
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
folder = "sessions_data"

if not os.path.exists(folder):
    os.makedirs(folder)

user_ids = [
    "5bde6480-0ab0-43b2-8529-ae22b458f836", "3ba5c0ca-2d1c-4d75-82b7-a2c821f2ea43", "d86a654c-f156-4873-9fec-b758bd53146a",
    "14ec54a1-24e9-462b-9378-3e9d812cba5a", "9b47b488-09f3-4d00-a56c-8c970bdfab8e", "111907fd-95b7-4729-a2af-e51ad656e288",
    "77f0712b-554f-4c5c-9898-14e7c77b26a0", "ffef8945-c190-4f95-930f-4e35c2e3a868", "aca50ebd-2a70-41b2-a3f9-1a2deecc8322",
    "4f113d91-1e3e-46f7-a9ca-95f02de96297", "aa76de66-83a4-4c21-92f5-cfe20525387a", "80d8a76b-4c97-4a12-9ac3-02a6d37e11a9",
    "ca9d1f5f-925b-4a59-b362-4703a75ad77c", "f25d6d08-ed4a-4680-b7e3-94d4b30207df", "31b1cad6-43b6-4fa7-95e5-7d79676b01e7",
    "f9c7e851-4d89-46ce-8678-25b88916a574", "9ce1bf0b-8366-40e1-b77c-9493a981c91b", "625ea2f3-d6f3-47f0-abd3-a204ea4eb491",
    "3da55713-36de-4077-9d4d-626d934aafe0", "37f86d6c-c234-4339-9c0f-ec3bdaab8536"
]

locations = [
    {"country": "USA", "latitude": 37.0902, "longitude": -95.7129},
    {"country": "Canada", "latitude": 56.1304, "longitude": -106.3468},
    {"country": "UK", "latitude": 51.5099, "longitude": -0.1181},
    {"country": "Germany", "latitude": 51.1657, "longitude": 10.4515},
    {"country": "France", "latitude": 48.8566, "longitude": 2.3522},
    {"country": "Italy", "latitude": 41.9028, "longitude": 12.4964},
    {"country": "Spain", "latitude": 40.4168, "longitude": -3.7038},
    {"country": "Australia", "latitude": -25.2744, "longitude": 133.7751},
    {"country": "Brazil", "latitude": -14.2350, "longitude": -51.9253},
    {"country": "India", "latitude": 20.5937, "longitude": 78.9629},
    {"country": "China", "latitude": 35.8617, "longitude": 104.1954},
    {"country": "Japan", "latitude": 36.2048, "longitude": 138.2529},
    {"country": "South Africa", "latitude": -30.5595, "longitude": 22.9375},
    {"country": "Russia", "latitude": 61.5240, "longitude": 105.3188},
    {"country": "Mexico", "latitude": 23.6345, "longitude": -102.5528}
]

def generate_path_counts(start_time):
    paths = ["/home", "/about", "/dashboard", "/profile", "/settings"]
    path_counts = {}
    
    for _ in range(random.randint(3, 6)):
        path = random.choice(paths)
        count = random.randint(1, 5)
        durations = [{"start": start_time, "end": start_time} for _ in range(count)]
        path_counts[path] = [{"count": count, "duration": durations}]
    
    return path_counts

def generate_session(date):
    start_time = int(date.timestamp() * 1000)
    end_time = start_time + random.randint(60000, 3600000)  # 1 min to 1 hour later
    location = random.choice(locations)  

    return {
        "start": int(date.timestamp()),
        "end": int((date + timedelta(minutes=random.randint(1, 60))).timestamp()),
        "bounce": {"isBounced": random.choice([True, False]), "pathname": "/frontend/index.html"},
        "device": random.choice(["Desktop", "Mobile", "Tablet", "Laptop"]),
        "browser": random.choice(["Mozilla", "Chrome", "Safari", "Edge"]),
        "location": {"latitude": location["latitude"], "longitude": location["longitude"], "country": location["country"]},
        "location": {"latitude": location["latitude"], "longitude": location["longitude"], "country": location["country"]},
        "uniqueId": random.choice(user_ids),
        "pathname": random.choice(["/frontend/index.html", "/home", "/dashboard", "/profile", "/settings"]),
        "language": random.choice(["en", "fr", "es", "de", "it", "zh", "ja"]),
        "referrer": random.choice(["Google", "Direct", "Social Media", "Email"]),
        "events": {key: random.randint(0, 10) for key in ["loadCount", "visibilitychangeCount", "resizeCount", "focusCount", "clickCount", "blurCount"]},
        "pageLoadTime": {"loadStart": start_time, "loadEnd": start_time + random.randint(1, 1000)},
        "productId": random.choice(["TRK-89olAsKyNOG7", "TRK-TlxlcwGkl19t", "TRK-Ob2CJVFgaau7"]),
        "pathCounts": generate_path_counts(start_time),
        "searchTerms": fake.sentence()
    }

def generate_data(start_date, days=1):
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        filename = os.path.join(folder, current_date.strftime("%y-%m-%d") + ".json")

        existing_data = []
        existing_data = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                existing_data = json.load(file)

        new_sessions = [generate_session(current_date) for _ in range(random.randint(5, 20))]

        with open(filename, "w") as file:
            json.dump(existing_data + new_sessions, file, indent=4)
            json.dump(existing_data + new_sessions, file, indent=4)

        print(f"Updated {filename} with {len(new_sessions)} new sessions (Total: {len(existing_data) + len(new_sessions)})")
        print(f"Updated {filename} with {len(new_sessions)} new sessions (Total: {len(existing_data) + len(new_sessions)})")

if not os.listdir(folder): 
if not os.listdir(folder): 
    generate_data(datetime.today() - timedelta(days=180), days=180)

generate_data(datetime.today(), days=1)
