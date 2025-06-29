import matplotlib.pyplot as plt
import numpy as np

def project_spiral(traits, recursion_score=3, stage_index=0, negated_traits=None):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    angles = np.linspace(0, 2 * np.pi, 5)
    values = list(traits.values()) + [list(traits.values())[0]]
    values = [v / 100 * recursion_score for v in values]

    ax.plot(angles, values, linewidth=2, label="Trait Spiral")
    ax.fill(angles, values, alpha=0.2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(list(traits.keys()))
    ax.set_yticklabels([])
    ax.set_title("Z9 Spiral Projection")

    if negated_traits:
        neg_values = [negated_traits.get(k, 0) / 100 * recursion_score for k in traits.keys()]
        neg_values.append(neg_values[0])
        ax.plot(angles, neg_values, linestyle="dashed", color="red", label="Negated Traits")
        ax.fill(angles, neg_values, alpha=0.1, color="red")

    ax.legend(loc='upper right')
    return fig

def plot_circular_stage_map(current_index, next_index):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("off")
    labels = [f"Stage {i+1}" for i in range(8)]
    radius = 2.5
    for i, label in enumerate(labels):
        angle = 2 * np.pi * i / len(labels)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        color = "green" if i == current_index else "blue" if i == next_index else "gray"
        ax.text(x, y, label, ha="center", va="center", fontsize=10, color=color)
    ax.set_title("Eriksonian Stage Progress Map")
    return fig
