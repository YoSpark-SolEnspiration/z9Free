import math

def map_disc_to_stage(d_score: float, i_score: float, s_score: float, c_score: float) -> str:
    """
    Map average DISC score to a Z9 Spiral stage (1–8) using floor scaling.
    """
    avg = (d_score + i_score + s_score + c_score) / 4.0
    norm = (avg - 1) / 4.0
    norm = max(0.0, min(norm, 1.0))
    stage_index = math.floor(norm * 8) + 1
    stage_index = min(stage_index, 8)
    return f"Stage {stage_index}"
