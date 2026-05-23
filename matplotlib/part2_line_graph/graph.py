import matplotlib.pyplot as plt


def show_graph(times, temperatures):

    plt.plot(times, temperatures, marker="o")

    plt.title("Temperature Trend Analysis")

    plt.xlabel("Time")

    plt.ylabel("Temperature")

    plt.grid(True)

    plt.show()