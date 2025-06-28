import json
from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data" / "tips.json"

def get_tip(answers):
    with open(DATA_PATH, "r") as f:
        tips = json.load(f)
    # Basic lookup—expand later by using `answers`
    return tips.get("default", "Keep shining your Z9 spark!")
