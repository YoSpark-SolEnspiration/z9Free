# trait_summary.py

from typing import Dict, Optional

def summarize_trait(
    traits: Dict[str, float],
    stage: Optional[str] = None,
    mood: Optional[int] = None
) -> str:
    """
    Identify the dominant DISC trait and return a rich summary message including
    growth path, caution flag, stage context, and a mood-based tip.

    Args:
        traits: Mapping of DISC trait labels ('D','I','S','C') to numeric values.
        stage: Optional spiral stage (e.g. "Stage 3").
        mood: Optional mood level (0–10).

    Returns:
        A formatted markdown string summarizing the trait, growth path, flag,
        plus optional stage context and mood-based insight.
    """
    # 1. Determine top trait
    top_trait = max(traits.keys(), key=lambda k: traits[k])
    score = traits[top_trait]

    # 2. Base summaries
    summaries: Dict[str, Dict[str, str]] = {
        "D": {
            "summary": "Direct, driven, and goal-focused.",
            "growth_path": "Develop trust by integrating patience and collaboration.",
            "development_flag": "Overdominance can suppress cooperation and empathy."
        },
        "I": {
            "summary": "Expressive, social, and inspiring.",
            "growth_path": "Grow by anchoring ideas in stability and routines.",
            "development_flag": "Overexpression can blur boundaries and decrease follow-through."
        },
        "S": {
            "summary": "Stable, supportive, and cooperative.",
            "growth_path": "Expand your comfort by embracing bold ideas and decisive leadership.",
            "development_flag": "Overreliance on routine can cause passivity or resistance to change."
        },
        "C": {
            "summary": "Precise, principled, and analytical.",
            "growth_path": "Build trust in self-expression and relational fluidity.",
            "development_flag": "Overstructure can cause perfectionism and emotional disconnect."
        }
    }

    data = summaries.get(top_trait)
    if not data:
        base_md = "You have a balanced personality."
        growth_md = ""
        flag_md = ""
    else:
        base_md = f"**{data['summary']}**  \n"
        growth_md = f"**Growth Path:** {data['growth_path']}  \n"
        flag_md = f"**Flag:** {data['development_flag']}  \n"

    # 3. Descriptor of trait level
    if score >= 4:
        level_desc = "high"
    elif score <= 2:
        level_desc = "low"
    else:
        level_desc = "moderate"
    level_md = f"Your {top_trait}-style score is {score}/5 ({level_desc}).  \n"

    # 4. Assemble core summary
    summary_md = base_md + growth_md + flag_md + level_md

    # 5. Append stage context
    if stage:
        summary_md += (
            f"At **{stage}**, a {level_desc} {top_trait} score suggests you’re "
            "well-positioned for this phase’s challenges.  \n"
        )

    # 6. Append mood-based insight
    if mood is not None:
        if mood <= 3:
            mood_tip = "You seem a bit low—consider celebrating small wins to boost momentum."
        elif mood >= 8:
            mood_tip = "You’re feeling great—now’s the time to tackle bigger goals!"
        else:
            mood_tip = "Your mood is balanced—strike a good mix of challenge and reflection."
        summary_md += f"{mood_tip}"

    return summary_md
