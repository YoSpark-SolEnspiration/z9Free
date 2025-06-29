import matplotlib.pyplot as plt

def generate_radar_chart(traits):
    """
    Generate a radar chart for DISC traits.
    """
    labels = list(traits.keys())
    values = list(traits.values())
    # Close the loop
    values += [values[0]]
    angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
    angles += [angles[0]]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])
    return fig
