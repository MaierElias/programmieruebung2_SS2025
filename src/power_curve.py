from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    data = load_data('data/activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])
    # Plotting the power curve
    time = np.arange(len(power_W))/60 # Convert to minutes
    fig, ax = plt.subplots()
    ax.plot(time, sorted_power_W[::-1], label='Power Curve')
    ax.set_xlabel('time / $min$')
    ax.set_ylabel('Power / $W$')
    ax.set_title('Power Curve')
    ax.plot(time, power_W[::+1], label='Original Power Curve')
    ax.legend(loc='upper right', fontsize='small')
    fig.savefig('figures/power_curve.png', dpi=300, bbox_inches='tight')

    plt.show()