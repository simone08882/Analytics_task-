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

def generate_path_counts():
    paths = ["/home", "/home/dashboard", "/login", "/home/create", "/profile", "/settings", "/cart", "/checkout"]
    return {random.choice(paths): random.randint(1, 10) for _ in range(random.randint(3, 6))}

def generate_session(date):
    return {
        "start": int(date.timestamp()),
        "end": int((date + timedelta(minutes=random.randint(1, 60))).timestamp()),
        "bounce": {"isBounced": random.choice([True, False]), "pathname": "/frontend/index.html"},
        "device": random.choice(["Desktop", "Mobile", "Tablet", "Laptop"]),
        "browser": random.choice(["Mozilla", "Chrome", "Safari", "Edge"]),
        "location": {"latitude": float(fake.latitude()), "longitude": float(fake.longitude())},
        "uniqueId": random.choice(user_ids),
        "pathname": random.choice(["/frontend/index.html", "/home", "/dashboard", "/profile", "/settings"]),
        "language": fake.language_code(),
        "referrer": fake.url() if random.choice([True, False]) else "",
        "events": {key: random.randint(0, 10) for key in ["loadCount", "visibilitychangeCount", "resizeCount", "focusCount", "clickCount", "blurCount"]},
        "pageLoadTime": {"loadStart": int(date.timestamp() * 1000), "loadEnd": int(date.timestamp() * 1000) + random.randint(1, 1000)},
        "productId": random.choice(["TRK-89olAsKyNOG7", "TRK-TlxlcwGkl19t", "TRK-Ob2CJVFgaau7"]),
        "pathCounts": generate_path_counts()
    }

def generate_past_data(start_date, days=180):
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        sessions = [generate_session(current_date) for _ in range(random.randint(5, 20))]

        filename = os.path.join(folder, current_date.strftime("%y-%m-%d") + ".json")

        with open(filename, "w") as file:
            json.dump(sessions, file, indent=4)

        print(f"Saved {len(sessions)} sessions to {filename}")

generate_past_data(datetime(2024, 9, 3))
