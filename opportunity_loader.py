# opportunity_loader.py

def load_basic_opportunities(traits: dict, mood: int, location: str = None) -> list[str]:
    """
    Returns a small set of actionable “opportunities” based on your primary DISC trait
    and current mood. This powers the Opportunity Snapshot.
    """
    # Determine primary trait
    primary = max(traits, key=traits.get)

    # Bucket mood into low/moderate/high
    if mood <= 3:
        bucket = "low"
    elif mood >= 8:
        bucket = "high"
    else:
        bucket = "moderate"

    # Static sample opportunities
    OPPS = {
        "D": {
            "low": [
                "Take a 5-minute pause before your next decision to stay clear-headed."
            ],
            "moderate": [
                "Lead a quick team brainstorm to test a small new idea."
            ],
            "high": [
                "Propose a mini-pilot project and outline next steps."
            ],
        },
        "I": {
            "low": [
                "Share one positive story with a colleague to reconnect."
            ],
            "moderate": [
                "Host a 2-minute icebreaker at your next meeting."
            ],
            "high": [
                "Organize a virtual coffee chat to grow your network."
            ],
        },
        "S": {
            "low": [
                "List three things you’re grateful for to boost calm."
            ],
            "moderate": [
                "Offer to help a teammate on their current task."
            ],
            "high": [
                "Volunteer to mediate a small group discussion."
            ],
        },
        "C": {
            "low": [
                "Review one routine you follow—can it be simplified?"
            ],
            "moderate": [
                "Create a checklist for an upcoming complex task."
            ],
            "high": [
                "Document a best-practice process and share it with your team."
            ],
        },
    }

    return OPPS.get(primary, {}).get(bucket, [])
