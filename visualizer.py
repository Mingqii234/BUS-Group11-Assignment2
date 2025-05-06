import matplotlib.pyplot as plt

class EnergyVisualizer:
    def plot_data_with_percent(self, data, title: str):
        total = sum(data)
        labels = list(range(len(data)))

        fig, ax = plt.subplots(figsize=(10,4))
        bars = ax.bar(labels, data)
        ax.set_title(title)
        ax.set_xlabel('Index')
        ax.set_ylabel('Energy Usage')
        ax.grid(True, axis='y', linestyle='--', alpha=0.5)

        for bar, value in zip(bars, data):
            pct = (value / total * 100) if total else 0
            ax.text(
                bar.get_x() + bar.get_width()/2,
                value * 1.01,
                f"{pct:.1f}%",
                ha='center', va='bottom', fontsize=8
            )

        plt.tight_layout()
        plt.show()