import json

def load_json_file(filepath: str):
    """Load and return JSON data from a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(data, filepath: str):
    """Save data as JSON to a file with indentation."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
