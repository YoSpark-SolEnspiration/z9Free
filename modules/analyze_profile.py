import json
import os

def analyze_profile(d, i, s, c, stage_label):
    """Analyze a DISC profile with Z9 logic and return detailed metrics."""
    total = d + i + s + c
    if total == 0:
        total = 1
    
    trait_percentages = {
        "D": round((d / total) * 100),
        "I": round((i / total) * 100),
        "S": round((s / total) * 100),
        "C": round((c / total) * 100)
    }

    # Subtrait approximation using pairing
    subtraits = {
        "DD": round(d * 0.6), "DI": round((d + i) / 2), "DS": round((d + s) / 2), "DC": round((d + c) / 2),
        "II": round(i * 0.6), "ID": round((i + d) / 2), "IS": round((i + s) / 2), "IC": round((i + c) / 2),
        "SS": round(s * 0.6), "SD": round((s + d) / 2), "SI": round((s + i) / 2), "SC": round((s + c) / 2),
        "CC": round(c * 0.6), "CD": round((c + d) / 2), "CI": round((c + i) / 2), "CS": round((c + s) / 2)
    }

    # Negated traits = low performers
    negated = {k: 100 - v for k, v in trait_percentages.items() if v < 25}

    # Harmony Ratio and Z9 Trait Score
    values = list(trait_percentages.values())
    avg = sum(values) / 4
    dev = sum(abs(v - avg) for v in values) / 4
    harmony_ratio = round(100 - dev, 2)
    trait_score = round((avg + harmony_ratio) / 2, 2)

    # Recursive dummy logic for now
    recursion_result = {
        "stable_score": round(trait_score / 10),
        "iterations": 4
    }

    # Remedy traits placeholder (requires remedy_traits.json)
    remedy_path = os.path.join("data", "remedy_traits.json")
    remedies = {}
    if os.path.exists(remedy_path):
        with open(remedy_path, "r") as f:
            remedy_data = json.load(f)
        for trait in trait_percentages:
            if trait in remedy_data:
                remedies[trait] = remedy_data[trait]

    # Product links placeholder (already stored in remedy file)
    product_links = []
    for trait, data in remedies.items():
        product_links.append({
            "title": f"{trait} Remedy",
            "link": data.get("product", "#")
        })

    return {
        "traits": trait_percentages,
        "subtraits": subtraits,
        "negated": negated,
        "harmony_ratio": harmony_ratio,
        "trait_score": trait_score,
        "recursion_result": recursion_result,
        "remedies": remedies,
        "product_links": product_links
    }
