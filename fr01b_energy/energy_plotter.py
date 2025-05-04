import matplotlib.pyplot as plt
import os

def plot_total_energy(buildings):
    labels = [b.id for b in buildings]
    values = [b.get_total_energy() for b in buildings]
    plt.bar(labels, values)
    plt.title("Total Energy by Building")
    plt.ylabel("kWh")
    plt.tight_layout()
    plt.savefig("output/total_energy_bar.png")
    plt.close()


def plot_device_trends(buildings):
    for b in buildings:
        for d in b.get_devices():
            usage = d.get_usage_by_day()
            dates = [d[0] for d in usage]
            values = [d[1] for d in usage]
            plt.plot(dates, values, marker="o", label=d.name)
        plt.title(f"{b.id} - Device Energy Trend")
        plt.xlabel("Date")
        plt.ylabel("kWh")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"output/{b.id}_trend.png")
        plt.close()


def plot_building_pie_charts(buildings):
    for b in buildings:
        breakdown = b.device_energy_breakdown()
        if breakdown:
            plt.pie(breakdown.values(), labels=breakdown.keys(), autopct="%1.1f%%")
            plt.title(f"{b.id} - Device Energy Proportion")
            plt.tight_layout()
            plt.savefig(f"output/{b.id}_pie.png")
            plt.close()