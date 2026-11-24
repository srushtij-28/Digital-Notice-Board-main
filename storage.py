import json
import os

DATA_FILE = "notices.json"


def load_notices():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_notices(notices):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(notices, file, indent=4)
